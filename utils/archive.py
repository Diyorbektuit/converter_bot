import zipfile
import os

BASE_DIR = os.getenv('BASE_DIR', "/home/diyorbek/PycharmProjects/converter_bot/")
print(BASE_DIR)

def convert_zip(file_path_list: list, zip_name: str):
    with zipfile.ZipFile(f"{BASE_DIR}{zip_name}", 'w') as zip_file:
        for file in file_path_list:
            arc_name = os.path.relpath(f"{BASE_DIR}{file}", start=os.path.dirname(f"{BASE_DIR}{file_path_list[0]}"))
            zip_file.write(file, arc_name)


file_paths = [f'downloads/file.py']
zip_name = f'downloads/archive/my_archive-1938.zip'
convert_zip(file_paths, zip_name)

def unzip_files(zip_name: str, extract_to: str):
    with zipfile.ZipFile(zip_name, 'r') as zip_file:
        zip_file.extractall(extract_to)


