
import logging
import os
from github_api_cls.workers.worker import WorkerRepos
from github_api_cls.db.db_setting import DB
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Orchestrator:

    def __init__(self, mode="simple", list_orgs=None):
        self.mode = mode
        self.list_orgs = list_orgs
        self.list_repos = []
        self.twenty_repos_max_stars = None
        self.cpu_count = os.cpu_count()

        if mode == "simple":
            self.start_simple()
        elif mode == "thread":
            self.start_thread()
        elif mode == "process":
            self.start_process()
        elif mode == "async":
            pass

        self.get_twenty_repos_max_stars()
        self.write_data_to_db()
        self.show_all_data()

    def start_simple(self):
        """Start executor without parallal processing data"""
        for orgs in self.list_orgs:
            worker = WorkerRepos(orgs)
            self.list_repos.extend(worker.list_repos)
        logging.info("Simple completed")

    def start_thread(self):
        """Start executor with thread parallal processing data"""
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_repos = {executor.submit(WorkerRepos, orgs): orgs for orgs in self.list_orgs}
            for future in as_completed(future_repos):
                orgs_login = future_repos[future]["login"]
                try:
                    data = future.result()
                    self.list_repos.extend(data.list_repos)
                except Exception as exc:
                    logging.critical('{} generated an exception: {}'.format(orgs_login, exc))
                else:
                    logging.info('{} page'.format(orgs_login))
        logging.info("Thread completed")

    def start_process(self):
        """Start executor with process parallal processing data"""
        with ProcessPoolExecutor(max_workers=self.cpu_count) as executor:
            future_repos = {executor.submit(WorkerRepos, orgs): orgs for orgs in self.list_orgs}
            for future in as_completed(future_repos):
                orgs_login = future_repos[future]["login"]
                try:
                    data = future.result()
                    self.list_repos.extend(data.list_repos)
                except Exception as exc:
                    logging.critical('{} generated an exception: {}'.format(orgs_login, exc))
                else:
                    logging.info('{} page'.format(orgs_login))
        logging.info("Process completed")

    # def async_process(self):
    #     """Start executor with async await processing data"""
    #     for orgs in self.list_orgs:
    #         worker = WorkerRepos(orgs, mode_request="async")
    #         self.list_repos.extend(worker.list_repos)
    #     logging.info("Async completed")

    def write_data_to_db(self):
        if self.twenty_repos_max_stars:
            session = DB()
            session.write_db(self.twenty_repos_max_stars)
        else:
            logging.info("self.twenty_repos_max_stars is empty")

    def show_all_data(self):
        session = DB()
        session.show_all()

    def get_twenty_repos_max_stars(self):
        self.twenty_repos_max_stars = sorted(self.list_repos,
                                             key=lambda repo: repo["stargazers_count"],
                                             reverse=True)[:20]
        logging.info("Twenty repos by max start completed")
