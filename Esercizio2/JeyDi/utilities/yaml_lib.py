import yaml
import os
import re
import pandas as pd
from utilities.utility import get_folder_path


def checkpath(to_path, filename):
    """
    Check path and filename
    """
    if to_path == '' or to_path is None:
        to_path = get_folder_path('./')

    if filename == '' or filename is None:
        filename = 'result.yml'

    if re.search(r"yml", filename) == False:
        filename = filename + '.yml'

    file_path = os.path.join(to_path, filename)

    return file_path


def read_yaml(file_path, filename=''):
    """
    Read a yaml file from disk
    """
    file_path = checkpath(file_path, filename)

    try:
        with open(file_path) as file:

            data = yaml.load(file, Loader=yaml.FullLoader)
            file.close()
        print(f"File succesfully readed")
        return data

    except Exception as message:
        print(f"Impossibile to read the file: {message}")
        return None


def write_dataset_yaml(to_path='', filename='', dataset=None):
    """
    Write a pandas dataset to yaml
    """
    file_path = checkpath(to_path, filename)

    if isinstance(dataset, pd.DataFrame) == False:
        print(f"Please use a Pandas dataframe with write_dataset_yaml function")
        return False

    try:
        with open(file_path, 'w') as file:
            documents = yaml.dump(dataset, file)
        file.close()
        print(f"File successfully write to: {file_path}")
        return True

    except Exception as message:
        print(f"Impossible to write the file: {message}")
        return False


def write_yaml(to_path, filename, obj_save):
    """
    Write some properties to generic yaml file
    :param to_path: where you want to save your file
    :param filename: name of the file
    :param obj_save: the object you want to save
    :return: a boolean with success or insuccess
    """
    file_path = checkpath(to_path, filename)

    try:
        with open(file_path, 'w') as file:
            documents = yaml.dump(obj_save, file)
        file.close()
        print(f"File successfully write to: {file_path}")
        return True

    except Exception as message:
        print(f'Impossible to write the file: {message}')
        return False
