import json
import uuid
import os


def read_json(path: str) -> list:
    """Read json file and return list with data"""

    with open(path, "r", encoding='utf-8') as file_json:
        return json.load(file_json)


def write_data_in_file(data_list: list) -> None:
    """Write result data in file."""

    file_name = uuid.uuid4().hex
    with open(f"data_result/{file_name}.json", "w", encoding='utf-8') as file_json:
        json.dump(data_list, file_json)

    print(f"File {file_name}.json created.")


def split_data(data_sourse: list) -> None:
    """Split data by 30 recorder."""

    folder_path = "data_result"
    if os.path.exists(folder_path):
        files = os.listdir(folder_path)
        for file_name in files:
            os.remove(f"{folder_path}/{file_name}")
    else:
        os.mkdir(folder_path)

    list_result = []

    for item, value in enumerate(data_sourse, 1):
        list_result.append(value)
        if item % 30 == 0:
            write_data_in_file(list_result)
            list_result.clear()

    print("Split complete")


def start_split_data(path_json: str) -> None:
    """Start script. In the parameter put the path to the file.
       For example: 'sourse/response_1633859991949.json' """

    data_list = read_json(path_json)
    split_data(data_list)

start_split_data("sourse/response_1633859991949.json")