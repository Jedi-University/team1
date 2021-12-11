""" This is the homework 7 modul with threads/multiprocessing.

"""
__version__ = '0.1'
__author__ = 'Popova Irene'

from workers.workerfetchorg import WorkerFetchOrg 
from workers.workerfetchrep import WorkerFetchRep
from workers.workerstore import WorkerStore
from workers.workershow import WorkerShow



class Orch():
    def __init__(self, workers: list, parameters: dict):
        self.status = True
        self.workers = workers
        self.parameters = parameters

    def set_worker_parameter(self, pair_change: dict):
        self.parameters.update(pair_change)

    def run(self):
        for i in self.workers:
           if self.status:
               i.update_parameters(self.parameters)
               i.run()
               self.status = i.status
               if len(i.out_result) > 0 :
                   self.parameters.update(i.out_result)
           else:
               print(f'Статус предыдущего этапа {self.status}')
                 
