""" This is the homework 7 modul for choicing organization from GitHub.
"""
__version__ = '0.1'
__author__ = 'Popova Irene'

import requests
import json

from github_object.getapiresult import getAPIresult


class OrgGithub():
    ''' Модель списка организации в GitHub
    '''
    
    def __init__(self, quantity_org):
        # quantity_org кол-во организаций, положительное  целое число 
        self.limit=100          # ограничения по количеству выдаваемых по запросам организаций
        self.url='https://api.github.com/organizations' # типовой запрос
        self.quantity = abs(int(quantity_org))
        self.fetch_status = 0        # статус запроса "ok" - 200   
        
    def fetching(self):
        ''' выбирает оquantity_org зарегистрированных организаций в GitHub
            и возвращает список из их названий
        '''
        if self.quantity < self.limit:
            org_limit = self.quantity
        else:
             org_limit = self.limit  
        quantity_proc = 0
        list_org = []
        while quantity_proc < self.quantity:
              quantitys = org_limit if (self.quantity > quantity_proc + org_limit) else (self.quantity - quantity_proc)
              if len(list_org) == 0:
                  url = self.url + '?per_page=' + str(quantitys)
              else:
                  korr_link = link.split('=')
                  last_quant=int(korr_link[1][:korr_link[1].find('&')])
                  url=link
                  if not last_quant == quantitys:
                      url = korr_link[0] + '=' + str(quantitys) + korr_link[1][korr_link[1].find('&'):] + '=' + korr_link[2]
              file_result = getAPIresult(url)
              result = file_result.json()
              self.fetch_status = file_result.status_code
              link=file_result.links ['next'] ['url'] if file_result.status_code ==200 else ""
              list_org.extend([j['login'] for j in result])
              quantity_proc += len(result)
        return list_org
    
    def fetching_status(self):
        ''' статус получения списка (успешно/ не успешно)
        '''       
        res_stat = False
        if self.fetch_status == 200:
            res_stat = True
            print(f'Выбрано {self.quantity} организаций')
        else:
            print('Ничего не выбрано')
        return res_stat
        

