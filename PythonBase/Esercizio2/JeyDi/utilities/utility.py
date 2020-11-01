import os


def get_folder_path(custom_path='', force_creation=False):
    """

    :param custom_path:
    :param force_creation:
    :return:
    """
    if custom_path is '' or custom_path is None:
        BASEPATH = os.path.abspath('')
    else:
        BASEPATH = os.path.abspath(custom_path)

    # Check if the folder exist, if not exit you can create with a flag
    if not os.path.exists(BASEPATH):
        print("WARNING: Path doesn't exist")
        if force_creation:
            print("Force creation folder")
            try:
                os.makedirs(BASEPATH)
            except Exception as message:
                print(f"Impossible to create the folder: {message}")

    print(f"PATH: {BASEPATH}, force creation: {force_creation}")
    return BASEPATH


def define_path(BASEPATH='', DATASET='test_data.xlsx', DATA_LOCATION='data', SEED=42):
    """
    Define a path for a file.
    INPUT: Basepath you want to search and dataset name plus a default location
    OUTPUT: the file path
    """

    if BASEPATH == '':
        BASEPATH = os.path.abspath('')

    # Set the default Data Path
    if DATA_LOCATION == '' or DATA_LOCATION is None:
        DATA_PATH = os.path.join(BASEPATH, DATASET)
    else:
        DATA_PATH = os.path.join(BASEPATH, DATA_LOCATION, DATASET)

    print(f"\n Dataset location: {DATA_PATH} \n")

    return DATA_PATH


def checkpath(to_path, filename):
    """
    Check path and filename
    """
    if to_path == '':
        to_path = get_folder_path('../../../../Corsi/Python/Esercizi/utilities/')

    if filename == '':
        print("Please insert a valid filename")
        return None

    file_path = os.path.join(to_path, filename)

    return file_path


def define_path(BASEPATH='', DATASET='test_data.xlsx', DATA_LOCATION=''):
    """
    Define a path for a file.
    INPUT: Basepath you want to search and dataset name plus a default location
    OUTPUT: the file path
    """

    if BASEPATH == '':
        BASEPATH = os.path.abspath('')

    # Set the default Data Path
    if DATA_LOCATION == '' or DATA_LOCATION is None:
        DATA_PATH = os.path.join(BASEPATH, DATASET)
    else:
        DATA_PATH = os.path.join(BASEPATH, DATA_LOCATION, DATASET)

    print(f"\n Dataset location: {DATA_PATH} \n")

    return DATA_PATH
