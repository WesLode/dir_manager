#! python3

import sys
import os
import shutil
import yaml

# from rename import rename
from group import  move_file
# import utils

def main_function():
    with open('local_config.yaml') as c_file:
        config = yaml.safe_load(c_file)

    # import sys, os
    print(os.getcwd())
    # os.chdir(os.path.expandvars(f'{main_path}{data1['dir']}'))
    # rename(config)
    move_file(config)

if __name__ == "__main__":
    main_function()
