# python get_data_json.py
import sys
import requests
import json
import os
import shutil
monet = "aave" 
days = 365
urlRequest = "https://api.coingecko.com/api/v3/coins/"+monet+"/ohlc?vs_currency=usd&days="+ str(days)
APIanswer = requests.get(urlRequest)
namedir = monet+"_for_"+str(days)+"_days"
filename=monet+"_OHLC_"+str(days)+".json"
filewithpath = namedir + "/" + filename
try:
    os.remove(filewithpath)
except OSError:
    pass
try:
    shutil.rmtree(namedir)
except OSError:
    pass
os.mkdir(namedir)
file_result = APIanswer.text
with open(filewithpath, "w") as fi:
    fi.write(file_result)
#

