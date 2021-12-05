""" This is the homework 7 modul with threads/multiprocessing.

"""
__version__ = '0.1'
__author__ = 'Popova Irene'

import time
import os
from  multiprocessing import Pool,Process, Queue
import threading
import queue

from github_object.my_objects import RepoGithub, OrgGithub
from db.db import db


class myThread (threading.Thread):
    def __init__(self, name, counter,name_org, count_top):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
        self.name_org = name_org
        self.count_top = count_top
        self.list_repos = []
    def run(self):
        temp_repos = RepoGithub(self.name_org, self.count_top)
        self.list_repos = temp_repos.fetching()

class Worker():
    ''' Abstract Class Worker
    '''
    def __init__(self ):
        self.status = False
        self.param = {}
        self.out_result = {}

    def UpdateParameters(self, param: dict ):
        self.param.update(param)
                
    def Run(self):
        pass
        
class WorkerFetchOrg(Worker):
    '''  Class Worker Fetching organization from GitHub
    '''
    def __init__(self, param: dict ):
        self.param = param
        self.get_quantity_org = param['get_quantity_org']
        self.fetch_list = []
        self.out_result = {'list_org':[]}
        self.listorgs = OrgGithub(self.get_quantity_org)
    
    def Run(self):
        self.fetch_list=self.listorgs.fetching()
        self.status=self.listorgs.fetching_status()
        self.out_result = {'list_org': self.fetch_list}
        
class WorkerFetchRep(Worker):
    '''  Class Worker Fetching repositiries from GitHub on threads
    '''
    def __init__(self, param: dict):
        self.param = param        
        self.count_top = param['count_top']
        self.list_org = param['list_org']
        self.out_result = {'list_repo':[]}
        self.status = False
        self.fetch_list = []

    def Run(self):
        # on threads
        self.list_org = self.param['list_org']
        if len(self.list_org) > 0:
            count_thread=os.cpu_count()*2
            print(f'ВЫбираю репозитории...')
            timing=time.time()
            ex_thread=list(i for i in range(count_thread)) 
            q_org=queue.Queue()
            for i in self.list_org:
                q_org.put(i)
            while not q_org.empty():
                for i in range(count_thread):
                    if q_org.empty():
                        exit
                    else:
                       name_org = q_org.get()
                       ex_thread[i] = myThread("Thread"+str(i+1), i+1, name_org, self.count_top)
                       ex_thread[i].start()
                for i in range(count_thread):
                    ex_thread[i].join()
                    self.fetch_list.extend(ex_thread[i].list_repos)
            self.fetch_list.sort(reverse = True)
            self.fetch_list = self.fetch_list[:20]
            self.out_result = {'list_repo': self.fetch_list}
            timing = round((time.time() - timing),2)
            print(f'ВЫбрано {len(self.fetch_list)} репозиториев за {timing} секунд')
            self.status = True if len(self.fetch_list)>0 else False
        else:
            self.status = False

            
class WorkerFetchRepOnMP(WorkerFetchRep):
    '''  Class Worker Fetching repositiries from GitHub on multiprocessing
    '''
    def __init__(self, param: dict):
        super().__init__(self, param)       
 
    def Run(self):
        # on multiprocessing
        self.list_org = self.param['list_org']
        if len(self.list_org) > 0:
            count_thread=multiprocessing.cpu_count()*2
            print(f'ВЫбираю репозитории...')
            timing=time.time()
            ex_thread=list(i for i in range(count_thread)) 
            q_org=Queue()
            for i in self.list_org:
                q_org.put(i)

                
            while not q_org.empty():
                for i in range(count_thread):
                    if q_org.empty():
                        exit
                    else:
                       name_org = q_org.get()
                # temp_repos = RepoGithub(self.name_org, self.count_top)
        # self.list_repos = temp_repos.fetching()
                       ex_thread[i] = Process(target = , args = (,))
 #                      ex_thread[i] = myThread("Thread"+str(i+1), i+1, name_org, self.count_top)
                       ex_thread[i].start()
                for i in range(count_thread):
                    ex_thread[i].join()
                    self.fetch_list.extend(ex_thread[i].list_repos)

                    
            self.fetch_list.sort(reverse = True)
            self.fetch_list = self.fetch_list[:20]
            self.out_result = {'list_repo': self.fetch_list}
            timing = round((time.time() - timing),2)
            print(f'ВЫбрано {len(self.fetch_list)} репозиториев за {timing} секунд')
            self.status = True if len(self.fetch_list)>0 else False
        else:
            self.status = False


class WorkerStore(Worker):
    '''  Class Worker saving into database
    '''
    def __init__(self, param: dict ):
        self.param = param  
        self.name_db = param['name_db']
        self.repos = param['list_repo']
        self.status = False
        self.my_db=db(self.name_db)
        self.out_result = {}

    def Run(self):
        self.repos = self.param['list_repo']        
        self.my_db.db_store(self.repos)
        self.status = True # ЭТО НЕПРАВИЛЬНО, ПЕРЕДЕЛАТЬ!!!!
    

class WorkerShow(Worker):
    '''  Class Worker selecting and printing
    '''
    def __init__(self, param: dict ):
        self.param = param 
        name_db = param['name_db']
        self.status = False
        self.my_db=db(name_db)
        self.out_result = {}

    def Run(self):
        self.my_db.db_show()
        self.status = True
        self.my_db.table_delete()                                                                                  

