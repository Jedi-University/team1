from get_data_json import start_get_data
from transform_data import start_split_data
from sma import calculate_and_write_sma_to_file


def start() -> None:
    """Start orchestrateur."""

    print("Start to get data.")
    result = start_get_data()
    print(f"Raw data extracted and wrote by path --> `{result.get('file_path')}`.")

    print("Start to split data.")
    start_split_data(result.get('file_path'))
    print("Split data completed and wrote to folder --> `result_split_data/`.")

    print("Start SMA30.")
    calculate_and_write_sma_to_file(result.get('raw_data_list'))
    print("SMA30 completed and result wrote to file by path --> `coin_folder/modified_ohlc.csv`.")


if __name__ == '__main__':
    start()