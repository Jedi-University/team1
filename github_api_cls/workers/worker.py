
import logging
from github_api_cls.api.request_api import RequestApi


logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class WorkerOrgs:

    def __init__(self, quantity_orgs):
        self.quantity_orgs = quantity_orgs
        self.max_orgs_on_page = 100
        if self.quantity_orgs < self.max_orgs_on_page:
            self.max_orgs_on_page = self.quantity_orgs
        self.url_orgs = f"https://api.github.com/organizations?per_page={self.max_orgs_on_page}"
        self.request_api = RequestApi()
        self.quantity_iter = self.get_quantity_iter()
        self.list_orgs = self.get_list_orgs()

    def get_quantity_iter(self):
        quantity_iter = self.quantity_orgs // self.max_orgs_on_page
        leftover_page = self.quantity_orgs % self.max_orgs_on_page
        if leftover_page > 0:
            quantity_iter += 1
        return quantity_iter

    def get_list_orgs(self):
        logging.info("Start get info about organisations.")
        tmp_list_orgs = []
        for _ in range(self.quantity_iter):
            answer_orgs = self.request_api.get_data_github_api(self.url_orgs)
            tmp_list_orgs.extend(answer_orgs.json())
            if answer_orgs.links.get("next", None):
                self.url_orgs = answer_orgs.links.get("next")["url"]
            else:
                break

        logging.info("Organizations list got.")
        return tmp_list_orgs


class WorkerRepos:

    def __init__(self, orgs, mode_request="simple"):
        self.url_repos = orgs["repos_url"]
        self.mode_request = mode_request
        self.flag = True
        self.request_api = RequestApi()
        self.list_repos = self.get_list_repos()

    def get_list_repos(self):
        logging.info("Start get info about repo each organization.")
        tmp_list_repo = []
        count_limit_request = 5  # You can put biggest number limit requests for repos
        count = 1
        while self.flag and count <= count_limit_request:
            answer_repos = self.request_api.get_data_github_api(self.url_repos)
            tmp_list_repo.extend(sorted(answer_repos.json(),
                                        key=lambda repo: repo["stargazers_count"],
                                        reverse=True)[:20])
            if answer_repos.links.get("next", None):
                self.url_repos = answer_repos.links.get("next")["url"]
            else:
                self.flag = False
            count += 1

        logging.info("Repo list got.")
        return sorted(tmp_list_repo,
                      key=lambda repo: repo["stargazers_count"],
                      reverse=True)[:20]


