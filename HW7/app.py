"""
Используя GitHub API для организаций (https://docs.github.com/en/rest/reference/orgs) 
для первых 200 организаций нужно подсчитать ТОП-20 самых "звездных" репозиториев
(т.е. те репозитории у которых больше всего звездочек среди всех организаций). 
Полученный ТОП нужно сохранить в базу используя SQLAlchemy в следующем формате Top(id, org_name, repo_name, stars_count). 
В приложение должно быть 2 команды 1 команда: fetch, которая забирает данные с github, находит ТОП и сохраняет его в базу; 
2 команда: show достает из базы ТОП и выводит на экран. 
В качестве базы нужно использовать sqllite.
"""
from github_object.my_objects import RepoGithub, OrgGithub
from db.db import db
from workers.workers import WorkerFetchOrg, WorkerFetchRep, WorkerStore, WorkerShow

# задаем имя бызы данных sqlite
my_home_db = 'sqlite:///homework.db'    
# задаем количество организаций, по которым будем проводить выбор ТОП репозиториев
quantity_org = 20
# задаем значение ТОП
quantity_top = 20

app_parameters = {'get_quantity_org': quantity_org,
                  'count_top': quantity_top,
                  'name_db' : my_home_db,
                  'list_org' : [],
                  'list_repo' : []}
app_workers = {'w1' : WorkerFetchOrg,
              'w3' : WorkerFetchRep,
              'w5' : WorkerStore,
              'w6' : WorkerShow }
app_orch = Orch(app_workers,app_parameters)
app_workers.update = {'w2' : app_orch.SetWorkerParameter({'list_org': worker1.fetch_list}),
                      'w4' : app_orch.SetWorkerParameter({'list_repo': worker2.fetch_list})
                     }
worker1 = WorkerFetchOrg(app_parameters) # init worker_list[0]
worker1.Run() #run worker_list[0]
worker1.status
app_parameters['list_org'] = worker1.fetch_list

worker2 = WorkerFetchRep(app_parameters) # init worker_list[1]
worker2.Run() # run worker_list[1]
worker2.status
app_parameters['list_repo'] = worker2.fetch_list

worker3 = WorkerStore(app_parameters) # init worker_list[2]
worker3.Run() # run worker_list[2]
worker3.status

worker4 = WorkerShow(app_parameters) # init worker_list[3]
worker4.Run() # run worker_list[3]
worker4.status

