"""
Используя GitHub API для организаций (https://docs.github.com/en/rest/reference/orgs) 
для первых 200 организаций нужно подсчитать ТОП-20 самых "звездных" репозиториев
(т.е. те репозитории у которых больше всего звездочек среди всех организаций). 
Полученный ТОП нужно сохранить в базу используя SQLAlchemy в следующем формате Top(id, org_name, repo_name, stars_count). 
В приложение должно быть 2 команды 1 команда: fetch, которая забирает данные с github, находит ТОП и сохраняет его в базу; 
2 команда: show достает из базы ТОП и выводит на экран. 
В качестве базы нужно использовать sqllite.
"""

from orch.orch import Orch
from workers.workerfetchorg import WorkerFetchOrg 
from workers.workerfetchrep import WorkerFetchRep
from workers.workerstore import WorkerStore
from workers.workershow import WorkerShow

# задаем имя бызы данных sqlite
my_home_db = 'sqlite:///homework.db'    
# задаем количество организаций, по которым будем проводить выбор ТОП репозиториев
quantity_org = 200
# задаем значение ТОП
quantity_top = 20
# определяем набор параметров приложения
app_parameters = {'get_quantity_org': quantity_org,
                  'count_top': quantity_top,
                  'name_db' : my_home_db,
                  'list_org' : [],
                  'list_repo' : []}
# определяем перечень воркеров приложения
worker1 = WorkerFetchOrg(app_parameters)
worker2 = WorkerFetchRep(app_parameters)
worker3 = WorkerStore(app_parameters)
worker4 = WorkerShow(app_parameters)
# определяем последовательность выполнения воркеров приложения
app_workers = [worker1, worker2, worker3, worker4]
# определяем оркестратор для реализации воркеров
app_orch = Orch(app_workers,app_parameters)
# запускаем оркестратор для реализации воркеров
app_orch.run()
