""" This is the homework 7 modul with threads/multiprocessing.

"""
__version__ = '0.1'
__author__ = 'Popova Irene'

from workers.workers import WorkerFetchOrg, WorkerFetchRep, WorkerStore, WorkerShow


class Orch():
    def __init__(self, workers: list, parameters: dict):
        self.status = True
        self.workers = workers
        self.parameters = parameters

    def SetWorkerParameter(self, PairChange: dict):
        self.parameters.update(PairChange)

    def Run(self):
        for i in self.workers:
           if self.status:
               i.UpdateParameters(self.parameters)
               i.Run()
               self.status = i.status
               if len(i.out_result) > 0 :
                   self.parameters.update(i.out_result)
           else:
               print(f'Статус предыдущего этапа {self.status}')
                 
