import sys
import requests
import json
import os
import shutil


def get_data_and_write_to_file() -> dict:
    monet = "aave"
    days = 365
    namedir = monet + "_for_" + str(days) + "_days"
    filename = monet + "_OHLC_" + str(days) + ".json"
    filewithpath = namedir + "/" + filename
    urlRequest = "https://api.coingecko.com/api/v3/coins/"+monet+"/ohlc?vs_currency=usd&days=" + str(days)
    raw_data_list = requests.get(urlRequest).json()

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
        json.dump(raw_data_list, fi, indent=4)

    return {
        "file_path": filewithpath,
        "raw_data_list": raw_data_list
    }


def start_get_data() -> dict:
    """Start get data by link and return current path on file with raw data"""

    return get_data_and_write_to_file()
