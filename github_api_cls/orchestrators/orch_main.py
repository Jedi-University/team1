from typing import List
import logging

from workers.worker import Worker

logger = logging.getLogger(__name__)


class Orchestrator:

    @staticmethod
    def schedule(workers: List[Worker]):
        """
            Run any workers.
            First iter put data which is None, because first worker have start data for processing.
        """

        data = None
        for worker in workers:
            logger.info(f"Start worker {worker}")
            data = worker.run(data=data)

