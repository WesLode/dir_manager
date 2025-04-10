import os
from utils import get_logger, get_time_stamp
import yaml

def default_config():
    with open('local_config.yaml') as c_file:
        config = yaml.safe_load(c_file)
    return config

def move_file(config = default_config()):
    data1 = config

    log = get_logger('File Sort')
    
    # list all file map
    file_dict = [{'file_path':dirpath,
                 'og_file':f,
                 'filter_keyword':[]}
                for (dirpath, dirnames, filenames) in os.walk(
                    f'{data1['parentDir']}\\{data1['dir']}'
                    ) for f in filenames 
                if "dir_manager" not in f]
    
    # get Map
    ext_map = dict()
    for i in data1['subcat']:
        ext_map[data1['subcat'][i]['name']] = data1['subcat'][i]['extension']
    
    # Check extension
    for file in file_dict:
        for ext in ext_map:
            if ext in file['file_path']:
                break
            if file['og_file'].split('.')[-1] in ext_map[ext]:
                file['update_file'] = f'{ext}\\{file['og_file']}'
                file['update'] = True
    
    update_list = [i for i in file_dict if i.get('update') is not None]

    # Undate file
    time_stamp = get_time_stamp()
    report_file = str()
    for item in update_list:
        og_name = f'{item['file_path']}\\{item['og_file']}'
        update_name = f'{item['file_path']}\\{item['update_file']}'
        report_file +=f'{time_stamp} {item['og_file']} has been updated to {item['update_file'].replace(item['og_file'],'')}\n'
        os.renames(og_name,update_name)
    
    for ext in ext_map:
        c = [i for i in update_list if ext in i['update_file']]
        log.info(f'{len(c)} file(s) has been moved to folder {ext}')
    
    with open('log/file_change.log','+a') as f1:
        text = f1.read()
        f1.write(f'{report_file}')

if __name__ == "__main__":
    move_file()
