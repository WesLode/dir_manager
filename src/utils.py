import uuid
import logging
import os
import time
from pathlib import Path


from datetime import datetime

class log_dir():
    def __init__(self):
        
        self.loc_dir = os.getcwd()
        self.detail_log_file = f'{self.loc_dir}\\log\\dir_manager_full.log'
        self.log_file = f'{self.loc_dir}\\log\\dir_manager_sum.log'

def get_time_stamp():
    return datetime.now().strftime(DATETIME_FORMAT)

def make_dir(path):
    directory_path = Path(path)

    try:
        directory_path.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        pass

def get_logger(name):
    make_dir(f'loglolol')
    loc_dir = os.getcwd()
    detail_log_file = f'{loc_dir}\\log\\dir_manager_full.log'
    log_file = f'{loc_dir}\\log\\dir_manager_sum.log'
    make_dir(f'{loc_dir}\\log')

    logger = logging.getLogger(name)
    # logger.setLevel('INFO')

    app_name = 'Directory Manager'
    formatter = logging.Formatter(f'<14>1 %(asctime)s.%(msecs)03dZ - {app_name} %(process)d - - %(levelname)s: (%(name)s) %(message)s',
                                      "%Y-%m-%dT%H:%M:%S")
    logging.basicConfig(filename=log_file, level=logging.DEBUG)
    
    formatter.converter = time.gmtime

    std_handler = logging.StreamHandler()
    std_handler.setLevel('INFO')
    std_handler.setFormatter(formatter)
    logger.addHandler(std_handler)

    file_handler = logging.FileHandler(detail_log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger



DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DATE_FORMATS = [
    '%Y-%m-%d',     # YYYY-MM-DD
    '%Y-%-m-%-d',   # YYYY-[M]M-[D]D
    '%m/%d/%Y',     # MM/DD/YYYY
    '%-m/%-d/%Y',   # [M]M/[D]D/YYYY
    '%Y/%m/%d',     # YYYY/MM/DD
    '%Y/%-m/%-d',   # YYYY/[M]M/[D]D
    '%Y%m%d',       # YYYYMMDD
    '%m-%d-%Y',     # MM-DD-YYYY
    '%-m-%-d-%Y',   # [M]M-[D]D-YYYY
    '%b %d %Y',     # MMM DD YYYY
    '%b %-d %Y',    # MMM [D]D YYYY
    '%d %b %Y',     # DD MMM YYYY
    '%-d %b %Y'     # [D]D MMM YYYY
]
DATETIME_FORMAT = '%Y%m%d-%H%M%S'

if __name__ == '__main__':
    log = get_logger('Test')
    log.debug('This is a debug message')
    log.info('This is an info message')
    log.warning('This is a warning message')
    log.error('This is an error message')
    log.critical('This is a critical message')