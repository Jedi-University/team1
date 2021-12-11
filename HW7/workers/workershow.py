""" This is the homework 7 modul with threads/multiprocessing.

"""
__version__ = '0.1'
__author__ = 'Popova Irene'


from db.db import Db
from workers.worker import Worker
   

class WorkerShow(Worker):
    '''  Class Worker selecting and printing
    '''
    def __init__(self, param: dict ):
        self.param = param 
        name_db = param['name_db']
        self.status = False
        self.my_db = Db(name_db)
        self.out_result = {}

    def run(self):
        self.my_db.db_show()
        self.status = True
        self.my_db.table_delete()                                                                                  

