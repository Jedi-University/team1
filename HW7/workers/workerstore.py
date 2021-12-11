""" This is the homework 7 modul with threads/multiprocessing.

"""
__version__ = '0.1'
__author__ = 'Popova Irene'

from workers.worker import Worker
from db.db import Db


class WorkerStore(Worker):
    '''  Class Worker saving into database
    '''
    def __init__(self, param: dict ):
        self.param = param  
        self.name_db = param['name_db']
        self.repos = param['list_repo']
        self.status = False
        self.my_db = Db(self.name_db)
        self.out_result = {}

    def run(self):
        self.repos = self.param['list_repo']        
        self.my_db.db_store(self.repos)
        self.status = True # ЭТО НЕПРАВИЛЬНО, ПЕРЕДЕЛАТЬ!!!!
    

