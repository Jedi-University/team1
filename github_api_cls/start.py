
from github_api_cls.workers.worker import WorkerOrgs
from github_api_cls.orchestrators.orch_main import Orchestrator
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main(start_mode, quantity_orgs):

    orgs = WorkerOrgs(quantity_orgs)
    Orchestrator(start_mode, orgs.list_orgs)


if __name__ == "__main__":

    """
    start_mode:
        simple - start simple mode without parallal processing data
        thread - start thread mode with parallal processing data
        process - start process mode with parallal processing data
        async - start async mode with (async await) processing data
    """

    # START_MODE = "simple"
    # START_MODE = "thread"
    START_MODE = "process"
    # START_MODE = "async"
    QUANTITY_ORGS = 200

    start_time = time.time()

    main(START_MODE, QUANTITY_ORGS)

    logging.info(f"App successfully passed. Time ran: {round(time.time() - start_time, 2)} sec.")