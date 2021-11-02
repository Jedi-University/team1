#
#Используя GitHub API для организаций (https://docs.github.com/en/rest/reference/orgs) 
#для первых 200 организаций нужно подсчитать ТОП-20 самых "звездных" репозиториев
#(т.е. те репозитории у которых больше всего звездочек среди всех организаций). 
#Полученный ТОП нужно сохранить в базу используя SQLAlchemy в следующем формате Top(id, org_name, repo_name, stars_count). 
#В приложение должно быть 2 команды 1 команда: fetch, которая забирает данные с github, находит ТОП и сохраняет его в базу; 
#2 команда: show достает из базы ТОП и выводит на экран. 
#В качестве базы нужно использовать sqllite.
#
from  top_repo_github import connection_db_and_table, get_org,fetching,show

# задаем имя бызы данных sqlite
my_home_db='sqlite:///homework.db'    
# задаем количество организаций, по которым будем проводить выбор ТОП репозиториев
get_quantity_org=10
#задаем значение ТОП
quantity_top=20
#fetch
# выбираем репозитории заданного количества организаций из GitHub,
# получаем из них ТОП-quantity_top, записываем все в базу данных
connection_db_and_table(my_home_db,get_quantity_org,quantity_top,fetching)
#show (выводим на экран из базы данных)
connection_db_and_table(my_home_db,get_quantity_org,quantity_top,show)
