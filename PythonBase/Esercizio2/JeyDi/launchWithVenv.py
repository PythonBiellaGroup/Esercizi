# Path to a Python interpreter that runs any Python script
# under the virtualenv /path/to/virtualenv/
import subprocess
from utilities.utility import get_folder_path

path = get_folder_path('./venv/bin/python')

# Path to the script that must run under the virtualenv
script_file = "./ContaParole.py"

subprocess.Popen([path, script_file])
