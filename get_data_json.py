import sys
import requests
import json
import os
import shutil


def get_data_and_write_to_file() -> str:
    monet = "aave"
    days = 365
    namedir = monet + "_for_" + str(days) + "_days"
    filename = monet + "_OHLC_" + str(days) + ".json"
    filewithpath = namedir + "/" + filename
    urlRequest = "https://api.coingecko.com/api/v3/coins/"+monet+"/ohlc?vs_currency=usd&days="+ str(days)
    raw_data = requests.get(urlRequest).text

    try:
        os.remove(filewithpath)
    except OSError:
        pass
    try:
        shutil.rmtree(namedir)
    except OSError:
        pass

    os.mkdir(namedir)
    with open(filewithpath, "w") as fi:
        fi.write(raw_data)

    return filewithpath


def start_get_data() -> str:
    """Start get data by link and return current path on file with raw data"""

    print("Start get data.")

    result_path = get_data_and_write_to_file()

    print(f"Raw data extracted and wrote by path '{result_path}'.")

    return result_path