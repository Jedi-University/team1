""" This is the homework 7 modul with threads/multiprocessing.

"""
__version__ = '0.1'
__author__ = 'Popova Irene'

class Worker():
    ''' Abstract Class Worker
    '''
    def __init__(self ):
        self.status = False
        self.param = {}
        self.out_result = {}

    def update_parameters(self, param: dict ):
        self.param.update(param)
                
    def run(self):
        pass
