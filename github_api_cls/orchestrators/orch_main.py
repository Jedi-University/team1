
from github_api_cls.db.db_setting import DB

import logging
logger = logging.getLogger(__name__)


class Orchestrator:

    @staticmethod
    def start_worker(worker):
        logger.info(f"Start worker {worker}")
        return worker.start_process()

    @staticmethod
    def get_top_twenty_repos(tmp_list_repo: list) -> list:
        logger.info(f"Get top twenty repos max stars")
        return sorted(tmp_list_repo,
                      key=lambda repo: repo["stargazers_count"],
                      reverse=True)[:20]

    @staticmethod
    def write_data_to_db(top_twenty_repos):
        if top_twenty_repos:
            session = DB()
            session.write_db(top_twenty_repos)
        else:
            logger.info("top_twenty_repos is empty")

    @staticmethod
    def show_all_data():
        session = DB()
        session.show_all()

