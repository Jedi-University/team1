
import logging
from github_api_cls.api.request_api import RequestApi


logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class WorkerOrgs():

    def __init__(self):
        self.quantity_orgs = 200
        self.quantity_iter = self.get_quantity_iter()
        self.start_org_id = 1
        self.max_orgs_on_page = 100
        self.url_orgs = "https://api.github.com/organizations"
        self.list_orgs = []

    def get_quantity_iter(self) -> int:
        quantity_iter = self.quantity_orgs // self.max_orgs_on_page
        leftover_page = self.quantity_orgs % self.max_orgs_on_page
        if leftover_page > 0:
            quantity_iter += 1
        return quantity_iter

    def get_list_orgs(self):
        logging.info("Start get info about organisations.")
        for _ in range(self.quantity_iter):
            url = self.get_next_page_url()
            request_api = RequestApi()
            batch_orgs = request_api.get_data_github_api(url)
            self.list_orgs.extend(batch_orgs)
            if self.list_orgs:
                self.start_org_id = self.list_orgs[-1]["id"]
        self.list_orgs = self.list_orgs[:self.quantity_orgs]
        logging.info("Organizations list got.")

    def get_next_page_url(self):
        url = f"{self.url_orgs}?since={self.start_org_id}&per_page={self.max_orgs_on_page}"
        return url


class WorkerRepos:

    def __init__(self):
        self.list_repos = []

    def get_list_repos(self, list_orgs):
        logging.info("Start get info about repo each organization.")
        for orgs in list_orgs:
            request_api = RequestApi()
            orgs_list_repo = request_api.get_data_github_api(orgs["repos_url"])
            self.list_repos.extend(sorted(orgs_list_repo, key=lambda repo: repo["stargazers_count"], reverse=True)[:20])
        twenty_repos_max_stars = sorted(self.list_repos, key=lambda repo: repo["stargazers_count"], reverse=True)[:20]
        logging.info("Repo list got.")
        return twenty_repos_max_stars

