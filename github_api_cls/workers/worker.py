
import requests
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

from decouple import config

import logging
logger = logging.getLogger(__name__)


GITHUB_TOKEN = config("github_token", default="")
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}


class Worker:
    """Abstract base class for workers"""

    def start_process(self):
        return self.get_list()

    def get_list(self):
        pass

    @staticmethod
    def get_data_by_url(url):
        answer = requests.get(url, headers=HEADERS)
        if answer.status_code == 200:
            return answer
        else:
            logger.warning(f"Not get data by api: "
                           f"status_code: {answer.status_code}; "
                           f"url {url}; "
                           f"answer_json: {answer.json()} ")


class WorkerOrgs(Worker):
    """Worker for get organizations"""

    def __init__(self, quantity_orgs):
        super().__init__()
        self.quantity_orgs = quantity_orgs
        self.max_orgs_on_page = 100
        if self.quantity_orgs < self.max_orgs_on_page:
            self.max_orgs_on_page = self.quantity_orgs
        self.url_orgs = f"https://api.github.com/organizations?per_page={self.max_orgs_on_page}"
        self.quantity_iter = self._get_quantity_iter()

    def _get_quantity_iter(self):
        quantity_iter = self.quantity_orgs // self.max_orgs_on_page
        leftover_page = self.quantity_orgs % self.max_orgs_on_page
        if leftover_page > 0:
            quantity_iter += 1
        return quantity_iter

    def get_list(self):
        logger.info("Start get info about organisations.")
        tmp_list_orgs = []
        for _ in range(self.quantity_iter):
            answer_orgs = self.get_data_by_url(self.url_orgs)
            if answer_orgs:
                tmp_list_orgs.extend(answer_orgs.json())
                if answer_orgs.links.get("next", None):
                    self.url_orgs = answer_orgs.links.get("next")["url"]
                else:
                    break

        logger.info("Organizations list got.")
        return tmp_list_orgs


class WorkerRepos(Worker):
    """Default worker for repos"""
    def __init__(self, list_orgs: list):
        super().__init__()
        self.list_orgs = list_orgs
        self.list_repos = []
        self.count_limit_request = 5  # You can put biggest number limit requests for repos

    def _get_list_repos(self, orgs):
        """Get list with repos organizations"""
        tmp_list = []
        flag_for_stop_iter = True
        url_repos = orgs["repos_url"]
        count = 1
        while flag_for_stop_iter and count <= self.count_limit_request:
            answer_repos = self.get_data_by_url(url_repos)
            if answer_repos:
                tmp_list.extend(sorted(answer_repos.json(),
                                       key=lambda repo: repo["stargazers_count"],
                                       reverse=True)[:20])
                if answer_repos.links.get("next", None):
                    url_repos = answer_repos.links.get("next")["url"]
                else:
                    flag_for_stop_iter = False
            else:
                flag_for_stop_iter = False
            count += 1
        return tmp_list

    def _start_parallel_executer_job(self, executor):
        """It for thread and process"""
        future_repos = {executor.submit(self._get_list_repos, orgs): orgs for orgs in self.list_orgs}
        for future in as_completed(future_repos):
            orgs_login = future_repos[future]["login"]
            try:
                data = future.result()
                self.list_repos.extend(data)
            except Exception as exc:
                logging.critical('{} generated an exception: {}'.format(orgs_login, exc))
            else:
                logging.info('{} page'.format(orgs_login))
            logger.info(f"Organization '{orgs_login}' ------> completed")


class WorkerReposSimple(WorkerRepos):
    """Worker for get repos without parallal"""

    def get_list(self):
        logger.info("Start get info about repo each organization.")

        for orgs in self.list_orgs:
            self.list_repos.extend(self._get_list_repos(orgs))

        logger.info("Repo list got.")
        return self.list_repos


class WorkerReposThread(WorkerRepos):
    """Worker for get repos with thread"""

    def get_list(self):
        logger.info("Start executor with thread parallal processing data")
        with ThreadPoolExecutor(max_workers=5) as executor:
            self._start_parallel_executer_job(executor)
        logger.info("Thread completed")
        return self.list_repos


class WorkerReposProcess(WorkerRepos):
    """Worker for get repos with process"""

    def __init__(self, list_orgs: list):
        super().__init__(list_orgs)
        self.cpu_count = os.cpu_count()

    def get_list(self):
        logger.info("Start executor with process parallal processing data")
        with ProcessPoolExecutor(max_workers=self.cpu_count) as executor:
            self._start_parallel_executer_job(executor)
        logger.info("Process completed")
        return self.list_repos

