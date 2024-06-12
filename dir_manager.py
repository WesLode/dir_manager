#! python3

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

def checkExtension(name, extensions):
    for i in extensions:
        if i in name:
            return True

def sortFile(orgpath, newpath, filter):
    if checkExtension(orgpath, filter):
        shutil.move(orgpath, f'{newpath}/{orgpath}')
        return True

def checkDir(dir_ext):
    if not os.path.exists(dir_ext):
        os.makedirs(dir_ext, mode=0o777)



def main():
    with open(config_file) as c_file:
        data1 = yaml.safe_load(c_file)
    os.chdir(os.path.expandvars(f'{main_path}{data1['dir']}'))
    listdir = os.listdir(os.getcwd())
    
    result_count = {}
    
    for sub_folder in data1['subcat']:
        checkDir(data1['subcat'][sub_folder]['name'])
        result_count[data1['subcat'][sub_folder]['name']] = 0


    for i in listdir:
        for sub_folder in data1['subcat']:
            if sortFile(i, data1['subcat'][sub_folder]['name'], data1['subcat'][sub_folder]['extension']):
                result_count[data1['subcat'][sub_folder]['name']] += 1

    for r in result_count:
        print(f'{result_count[r]} files has been moved to {r}')


if __name__ == "__main__":
    main()
