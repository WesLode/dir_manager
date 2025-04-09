#! python3

import sys
import os
import shutil
import yaml

def default_config():
    with open('local_config.yaml') as c_file:
        config = yaml.safe_load(c_file)
    return config

def rename(config = default_config()):
    data1 = config
    
    # list all file map
    file_dict = [{'file_path':dirpath,
                 'og_file':f,
                 'filter_keyword':[]}
                for (dirpath, dirnames, filenames) in os.walk(
                    f'{data1['parentDir']}\\{data1['dir']}'
                    ) for f in filenames 
                if "dir_manager" not in f]
    
    # Create rename map
    name_filter = dict()
    for j in data1['rename']:
        if data1['rename'][j]['old'] =='whitespace':
            name_filter[' '] = ''
        elif data1['rename'][j]['old'] is not None:
            name_filter[data1['rename'][j]['old']] = data1['rename'][j]['new']
    
    # analysis the directory, locate update file
    for j in file_dict:
        for item in name_filter:
            if item in j['og_file']:
                if j.get('update') is None: 
                    j['update_file'] = j['og_file']
                    j['update'] = True
                j['filter_keyword'] +=[item]
                j['update_file']=j['update_file'].replace(item,name_filter[item])
                
    u = [i for i in file_dict if i.get('update') is not None]

    # Undate file
    for item in u:
        og_name = f'{item['file_path']}\\{item['og_file']}'
        update_name = f'{item['file_path']}\\{item['update_file']}'
        os.renames(og_name,update_name)

    return file_dict

if __name__ == "__main__":
    rename()
