from db.db_setting import DB
from workers.worker import WorkerOrgs, WorkerReposSimple, WorkerWriteDataToDB, \
    WorkerReposThread, WorkerReposProcess, WorkerGetTop, WorkerAsyncRepos
from orchestrators.orch_main import Orchestrator
import time
import argparse
import sys

import logging
logging.basicConfig(level=logging.DEBUG, filename='logger/github_api.log',
                    format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)


class Main:
    """Start application which get data by github API"""

    def __init__(self, quantity_orgs):
        self.quantity_orgs = quantity_orgs
        self.start_time = None
        self.end_time = None
        self.orchestrator = Orchestrator()
        self.top_twenty_repos = []

    def start_app(self, mode) -> None:
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

    parser = argparse.ArgumentParser(description="Get data from github API")
    parser.add_argument("--orgs",
                        type=int,
                        required=True,
                        help="Quantity of organizations which you want to get their repositories")
    parser.add_argument("--mode",
                        type=str,
                        required=True,
                        help="simple - start simple mode without parallal processing data; "
                             "thread - start thread mode with parallal processing data; "
                             "process - start process mode with parallal processing data; "
                             "async - start async mode with (async await) processing data.")

    args = parser.parse_args(sys.argv[1:])
    main = Main(args.orgs)
    main.start_app(args.mode)
