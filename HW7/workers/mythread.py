""" This is the homework 7 modul with threads/multiprocessing.

"""
__version__ = '0.1'
__author__ = 'Popova Irene'


import threading
from github_object.repogithub import RepoGithub

class MyThread (threading.Thread):
    def __init__(self, name, counter,name_org, count_top):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
        self.name_org = name_org
        self.count_top = count_top
        self.list_repos = []
    def run(self):
        temp_repos = RepoGithub(self.name_org, self.count_top)
        self.list_repos = temp_repos.fetching()

        
        
