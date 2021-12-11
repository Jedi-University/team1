""" This is the homework 7 modul for choicing organization from GitHub.
    Your Token must be in a file in the format:
    myauth=('<name>','<token>')
"""
__version__ = '0.1'
__author__ = 'Popova Irene'

import requests
import json

from my_auth import myauth


def getAPIresult(url):
      APIanswer = requests.get(url,auth=myauth)
      return APIanswer


