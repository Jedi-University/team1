from github_api_cls.db.db_setting import DB
from workers.worker import WorkerOrgs, WorkerReposSimple, WorkerWriteDataToDB, \
    WorkerReposThread, WorkerReposProcess, WorkerGetTop, WorkerAsyncRepos
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
        self.top_twenty_repos = []

    def start_app(self, mode):
        if not isinstance(self.quantity_orgs, int) and self.quantity_orgs <= 0:
            logger.warning("Not correctly formatted paramert quantity orgs")
            exit()

        self.start_time = time.time()
        logger.info(f"Start app with mode '{mode}'.")

        worker_repos = {
            "simple": WorkerReposSimple(),
            "thread": WorkerReposThread(),
            "process": WorkerReposProcess(),
            "async": WorkerAsyncRepos(),
        }

        workers = [
            WorkerOrgs(self.quantity_orgs),
            worker_repos[mode],
            WorkerGetTop(),
            WorkerWriteDataToDB()
        ]

        self.orchestrator.schedule(workers)

        session = DB()
        session.show_all()

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
    main.start_app("simple")
    # main.start_app("thread")
    # main.start_app("process")
    # main.start_app("async")
