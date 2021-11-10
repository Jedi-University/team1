
from workers.worker import WorkerOrgs, WorkerReposSimple, WorkerReposThread, WorkerReposProcess
from orchestrators.orch_main import Orchestrator
import time

import logging
logging.basicConfig(level=logging.DEBUG, filename='logger/github_api.log',
                    format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)


class Main:
    def __init__(self, quantity_orgs: int = 0):
        self.quantity_orgs = quantity_orgs
        self.start_time = None
        self.end_time = None
        self.orchestrator = Orchestrator()
        self.orgs = WorkerOrgs(self.quantity_orgs)
        self.top_twenty_repos = []

    def start_app(self, mode):
        if not isinstance(self.quantity_orgs, int) and self.quantity_orgs <= 0:
            logger.warning("Not correctly formatted paramert quantity orgs")
            exit()

        self.start_time = time.time()
        logger.info(f"Start app with mode '{mode}'.")

        list_orgs = self.orchestrator.start_worker(self.orgs)

        repos = {
            "simple": WorkerReposSimple(list_orgs),
            "thread": WorkerReposThread(list_orgs),
            "process": WorkerReposProcess(list_orgs)
        }

        list_repos = self.orchestrator.start_worker(repos[mode])
        if list_repos:
            self.top_twenty_repos = self.orchestrator.get_top_twenty_repos(list_repos)
            self.orchestrator.write_data_to_db(self.top_twenty_repos)
            self.orchestrator.show_all_data()
        else:
            logger.warning("list_repos is empty")

        self.end_time = time.time()
        logger.info(f"App with mode '{mode}' successfully passed. Time ran: {round(self.end_time - self.start_time, 2)} sec.")


if __name__ == "__main__":
    """
        start_mode:
            simple - start simple mode without parallal processing data
            thread - start thread mode with parallal processing data
            process - start process mode with parallal processing data
            # (DONT'T WORK - IT IS IN THE JOB) async - start async mode with (async await) processing data
            
            QUANTITY_ORGS = 1 quantity organisations which do you want to get
    """

    QUANTITY_ORGS = 200

    main = Main(QUANTITY_ORGS)
    # main.start_app("simple")
    # main.start_app("thread")
    main.start_app("process")
