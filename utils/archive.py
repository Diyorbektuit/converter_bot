import zipfile
import subprocess
import os


def create_zip(file_paths: list, zip_name:str):
    try:
        zip_path = os.path.join(os.getcwd(), zip_name)
        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            for file_path in file_paths:
                if os.path.exists(file_path):
                    zip_file.write(file_path, os.path.basename(file_path))
        return zip_path
    except:
        return None


def unzip_files(zip_name: str, extract_to: str):
    with zipfile.ZipFile(zip_name, 'r') as zip_file:
        zip_file.extractall(extract_to)


def create_rar_archive(input_files: list, rar_name: str):
    try:
        rar_path = os.path.abspath(rar_name)
        valid_files = [os.path.abspath(file) for file in input_files if os.path.exists(file)]
        if not valid_files:
            print("Error: No valid files to add.")
            return None
        rar_cmd = ['rar', 'a', '-ep', rar_path] + valid_files
        result = subprocess.run(rar_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return rar_path
        else:
            print(f"Error creating RAR archive: {result.stderr.decode()}")
            return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

