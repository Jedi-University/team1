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
import requests
import json
import time
import sqlite3

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

def mapfunc(org_N):
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
# сортировка неправильная, переделать
# вставляем полученные данные в таблицу ТОП20
      counter=0 
      for i in l[:20]:
#          print(f"Записываю {i[2]} - {i[3]}")
          counter+=1
          j=[tuple([counter]+i)]
          print(f"Записываю {j}")
          my_cur.executemany("INSERT INTO TOP20(topid, stars_count,id, org_name, repo_name) VALUES(?,?,?,?,?);",j)
          conn.commit()
      return 

def print_from_db():
# выводим на печать из базы
#ПЕРЕДЕЛАТЬ ВЫВОД!!!!!!!!!!!!!!!!!!!
    my_cur.execute("""SELECT * FROM  TOP20;""")
    a=my_cur.fetchmany(20)
    print(a)

#спрятать токен в переменную окружения !!!!!!!!!!!!!!!!!!
myauth=('Pire66','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')
#подключаемся к базе данных homework.db
# создаем таблицу TOP20(id, org_name, repo_name, stars_count)
conn = sqlite3.connect('homework.db')
my_cur = conn.cursor()
my_cur.execute("""CREATE TABLE IF NOT EXISTS
            TOP20(topid INT PRIMARY KEY,id INT, org_name TEXT, repo_name TEXT, stars_count INT);""")
conn.commit()

file_result=getAPIresult('https://api.github.com/organizations?per_page=10')
result=file_result.json()
org200=[j['login'] for j in result]
file_result=getAPIresult('https://api.github.com/organizations?per_page=10&since='+str(org200[-1]))
result=file_result.json()
org200.extend([j['login'] for j in result])
#allrep=list(map(mapfunc,org200))
mapfunc(org200)
print_from_db()
my_cur.execute("DROP TABLE TOP20")
#
