import sys
import os
import shutil
import yaml

main_path = 'C:\\Users\\$USERNAME\\'

config_file = 'local_config.yaml'


def listDirectories():
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x)

def reset():
    with open(config_file) as c_file:
        data1 = yaml.safe_load(c_file)
    for i in data1['subcat']:
        os.chdir(os.path.expandvars(f'{main_path}{data1['dir']}\\{data1['subcat'][i]['name']}'))

        listdir = os.listdir(os.getcwd())
        for i in listdir:
            shutil.move(i, f'..\\{i}')


if __name__ == "__main__":
    reset()