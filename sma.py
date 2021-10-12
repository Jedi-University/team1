import os
import json
import csv
from systems import create_or_clear_folder


def sma(data):
    acc = 0
    for i in data:
        acc += i[4]
    return acc / len(data)


def data_filter(data):
    acc = []
    for i in data:
      if i[4] > sma(data):
         acc.append(i)
    return acc


def calculate_and_write_sma_to_file(raw_data: list) -> None:
    """Calculate sma and write result data to file."""

    directory_str = "coin_folder"
    filtered_file = "modified_ohlc.csv"
    filtered_file_path = directory_str + "/" + filtered_file

    create_or_clear_folder(directory_str)

    with open(filtered_file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        result_data = data_filter(raw_data)
        header = ["time", "open", "high", "low", "close"]
        writer.writerow(header)
        writer.writerows(result_data)