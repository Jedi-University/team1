#TOP20GitHub.py
#
#Используя GitHub API для организаций (https://docs.github.com/en/rest/reference/orgs) 
#для первых 200 организаций нужно подсчитать ТОП-20 самых "звездных" репозиториев
#(т.е. те репозитории у которых больше всего звездочек среди всех организаций). 
#Полученный ТОП нужно сохранить в базу используя SQLAlchemy в следующем формате Top(id, org_name, repo_name, stars_count). 
#В приложение должно быть 2 команды 1 команда: fetch, которая забирает данные с github, находит ТОП и сохраняет его в базу; 
#2 команда: show достает из базы ТОП и выводит на экран. 
#В качестве базы нужно использовать sqllite.
#
#import requests
#import json
#import time
#import sqlite3
import top_repo_github
from my_config import myauth


# задаем количество организаций, по которым будем проводить выбор ТОП репозиториев
get_quantity_org=10
#задаем значение ТОП
quantity_top=20
# выбираем заданное количество организаций из GitHub
list_org=top_repo_github.get_org(get_quantity_org)
# выбираем репозитории заданного количества организаций из GitHub, получаем из них ТОП-quantity_top, записываем все в базу данных
top_repo_github.fetch(list_org,quantity_top)
#выводим на экран из базы данных
top_repo_github.show(quantity_top)
