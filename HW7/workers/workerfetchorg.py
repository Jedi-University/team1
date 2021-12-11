""" This is the homework 7 modul with threads/multiprocessing.

"""
__version__ = '0.1'
__author__ = 'Popova Irene'

from github_object.orggithub import OrgGithub
from workers.worker import Worker

        
class WorkerFetchOrg(Worker):
    '''  Class Worker Fetching organization from GitHub
    '''
    def __init__(self, param: dict ):
        self.param = param
        self.get_quantity_org = param['get_quantity_org']
        self.fetch_list = []
        self.out_result = {'list_org':[]}
        self.listorgs = OrgGithub(self.get_quantity_org)
    
    def run(self):
        self.fetch_list = self.listorgs.fetching()
        self.status = self.listorgs.fetching_status()
        self.out_result = {'list_org': self.fetch_list}
        
