#Используя GitHub API для организаций (https://docs.github.com/en/rest/reference/orgs) 
#для первых N организаций нужно подсчитать ТОП-M самых "звездных" репозиториев
#(т.е. те репозитории у которых больше всего звездочек среди всех организаций). 
#Полученный ТОП  сохранить в базу используя SQLAlchemy в следующем формате Top(id, org_name, repo_name, stars_count). 
#В приложение должно быть 2 команды 1 команда: fetch, которая забирает данные с github, находит ТОП и сохраняет его в базу; 
#2 команда: show достает из базы ТОП и выводит на экран. 
#В качестве базы  используется sqllite.

from my_config import myauth
import requests
import json
import time
#import sqlalchemy
from sqlalchemy import create_engine, insert, select, MetaData, Table, Column,Text, Integer,ARRAY
from sqlalchemy import delete

# ограничения по количеству выдаваемых по запросам организаций и репозиториев
rep_limit=100

def waiting_n_minut(func):
    #ДОБИТЬ!!!!!!!!!!!!!!
    def wrapper(*args,**kwargs):
        answer=func(*args)
        if answer.status_code==403:
           print("Status code:",answer.status_code)
           get_limit = requests.get('https://api.github.com/rate_limit').json()
           while   answer.status_code==403 and get_limit['resources']['core']['remaining']==0:
              print("Waiting, min: ",(get_limit['resources']['core']['reset']-time.time())/60)
              time.sleep((get_limit['resources']['core']['reset']-time.time())/20)
              answer=func(*args)
        return_value=func(*args)
        return return_value
    return wrapper


#@waiting_n_minut
def getAPIresult(url):
      APIanswer = requests.get(url,auth=myauth)
      return APIanswer

def get_org(quantity_org):
    ''' выбирает оquantity_org зарегистрированных организаций в GitHub
        и возвращает список из их названий'''
    # ограничения по количеству выдаваемых по запросам организаций
    org_limit=100
    if quantity_org<org_limit:
        org_limit=quantity_org
    quantity_proc=0
    list_org=[]
    while quantity_proc<quantity_org:
        quantitys=org_limit if (quantity_org>quantity_proc+org_limit) else (quantity_org-quantity_proc)
        url='https://api.github.com/organizations?per_page='+str(quantitys)
        if len(list_org)>0:
            url+='&since='+str(result[-1]['id'])
        file_result=getAPIresult(url)
        result=file_result.json()
        list_org.extend([j['login'] for j in result])
        quantity_proc+=len(result)
        print(f'Выбрано {quantity_proc} организаций')
    return list_org


def connection_db_and_table(name_database,q_org,q_top,func):
    name_db=name_database
    engine=create_engine(name_db)
    my_conn=engine.connect()
    metadata = MetaData()
    name_table = Table('topn', metadata,
                 Column('topid',Integer(), primary_key=True ),
                 Column('id',Integer() ),
                 Column('org_name', Text() ),
                 Column('repo_name', Text() ),
                 Column('stars_count', Integer() )
                 )
    func(my_conn,name_table,q_org,q_top)

def fetching(my_conn,name_table,q_org,count_top):
#fetch вызывается из connection_db_and_table, 4-й аргумент
    org_N=get_org(q_org)
    l=[]
    for i in org_N:
        print(f"Обрабатываю {i}")
        file_result=getAPIresult('https://api.github.com/orgs/'+i+'/repos').json()
        for j in file_result:
            if j['stargazers_count']>0:
                dop=[j['stargazers_count'], j['id'], j['owner']['login'], j['name']]
                print(dop)
                l.append(dop)
    l.sort(reverse=True)
    counter=0 
    for i in l[:count_top]:
        counter+=1
        j=[counter]+i
        print(f"Записываю {j}")
        a=[{"topid": j[0],"id": j[2],"org_name": j[3],"repo_name": j[4],"stars_count": j[1]}]
        ins=insert(name_table)
        r=my_conn.execute(ins,a)

def show(my_conn,name_table,q_org,count_top):
#show вызывается из connection_db_and_table, 4-й аргумент
    s=name_table.select()
    r=my_conn.execute(s)
    print(f'TOP-{count_top} самых популярных репозиториев {q_org} организаций:')
    for i in r.fetchall():
        print(i)
    s=delete(name_table).where(name_table.c.topid > 0)
    r=my_conn.execute(s)


                                                                                  

