""" This is the homework 7 modul with threads/multiprocessing.
"""
__version__ = '0.1'
__author__ = 'Popova Irene'

from sqlalchemy import create_engine, MetaData, Table, Column,Text, Integer,ARRAY
from sqlalchemy import insert, select, delete


class Db():
    ''' Модель  таблицы в универсальной базе данных
        для демонстрации данных, полученных из GitHub
    '''
    def __init__(self, name_database):
        # создаем таблицу top_n
        self.name_db = name_database
        engine = create_engine(self.name_db)
        self.my_conn = engine.connect()
        metadata = MetaData()
        self.name_table = Table('top_n', metadata,
                  Column('topid', Integer(), primary_key=True, autoincrement = True ),
                  Column('id', Integer() ),
                  Column('org_name', Text() ),
                  Column('repo_name', Text() ),
                  Column('stars_count', Integer() ) )
        metadata.create_all(engine)

    def db_store(self, list_repo: list):
        # записываем в таблицу информацию из списка
       if len(list_repo) > 0:
          for j in list_repo:
              print(f"Записываю {j}")
              a = [{"id": j[1],
                 "org_name" : j[2],
                 "repo_name" : j[3],
                 "stars_count" : j[0]}
                ] 
              ins = insert(self.name_table)
              r = self.my_conn.execute(ins,a)

    def db_show(self):
    # выводим из таблицы ранее сохраненную информацию
        s = self.name_table.select()
        r = self.my_conn.execute(s)
        print('TOP самых популярных репозиториев организаций:')
        for i in r.fetchall():
           print(f'{i[4]:8} {i[1]:10} {i[2]:30} {i[3]:20}')


    def table_delete(self):
        # удаляем из таблицы все записи
        s = delete(self.name_table).where(self.name_table.c.topid > 0)
        r = self.my_conn.execute(s)           
