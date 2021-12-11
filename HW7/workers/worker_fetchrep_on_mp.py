""" This is the homework 7 modul with threads/multiprocessing.

"""
__version__ = '0.1'
__author__ = 'Popova Irene'

import time
import os
from  multiprocessing import Pool,Process, Queue

from github_object.my_objects import RepoGithub, OrgGithub
from workers.worker import Worker
from workers.workerfetchrep import WorkerFetchRep  
       
            
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


