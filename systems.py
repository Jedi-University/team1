import os


def create_or_clear_folder(folder_path: str) -> None:
    """Create folder if doesn't exists.
       If the folder exists then clear it."""

    if os.path.exists(folder_path):
        files = os.listdir(folder_path)
        for file_name in files:
            os.remove(f"{folder_path}/{file_name}")
    else:
        os.mkdir(folder_path)