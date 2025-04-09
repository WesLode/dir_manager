#! python3

import sys
import os
import shutil
import yaml

from src.rename import rename
from src.group import  move_file
import src.utils

def main():
    with open('local_config.yaml') as c_file:
        config = yaml.safe_load(c_file)
    rename(config)
    move_file(config)

if __name__ == "__main__":
    main()
