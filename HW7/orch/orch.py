""" This is the homework 7 modul with threads/multiprocessing.

"""
__version__ = '0.1'
__author__ = 'Popova Irene'


class Orch():
    def __init__(self, workers: dict, parameters: dict):
        self.status = []
        self.workers = workers
        self.parameters = {}

    def SetWorkerParameter(self, PairChange: dict):
        self.parameters.update(PairChange)

    def Run(self):
         
         pass
         
         
                 
