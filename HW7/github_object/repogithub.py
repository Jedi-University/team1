""" This is the homework 7 modul for choicing organization from GitHub.
"""
__version__ = '0.1'
__author__ = 'Popova Irene'

import requests
import json

from github_object.getapiresult import getAPIresult
from github_object.repoobj import RepoObj
        

class RepoGithub(RepoObj):
    ''' Модель репозиториев организации в GitHub
    '''
    
    def __init__(self, name_org, count_top):
        # ограничения по количеству выдаваемых по запросам организаций
        super().__init__()
        self.limit = 100
        self.org_name = name_org
        self.count_top = count_top
        # типовой запрос
        self.url = 'https://api.github.com/orgs/' + self.org_name + '/repos'
        self.fetch_status = 0

    def fetching(self):
        ''' выбирает все репозитории организации в GitHub
            и возвращает список из count_top ТОП
        '''
        list_repo = []
        file_result = getAPIresult(self.url)
        result = file_result.json()
        self.fetch_status = file_result.status_code
        dop = []
        for j in result:
            super().getrepo(j)
            if self.stargazers_count > 0:
                dop = [self.stargazers_count,
                       self.id,
                       self.owner,
                       self.name
                      ]
                list_repo.append(dop)
        list_repo.sort(reverse = True)      
        return list_repo[:self.count_top]
 
    def fetching_status(self):
        if self.fetch_status == 200:
             print(f'Выбрано {self.count_top} лучших репозиториев')
        else:
            print('Ничего не выбрано')
        return self.fetch_status


