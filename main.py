#! python3

import sys
import os
import shutil
import send2trash

emote_ext = ['png', 'jpg', 'gif']
rar_ext = ['rar', 'zip']

main_path = 'C:\\Users\\$USERNAME\\'
cus_path = 'C:\\Users\\test'
def listDirectories():
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x)

def checkExtension(name, extensions):
    for i in extensions:
        if i in name:
            return True


def main():
    sub_dir = 'Downloads'
    os.chdir(os.path.expandvars(f'{main_path}Downloads'))
    # listDirectories()
    dir_ext = 'pic_emote'
    sub_dir_ext = f'{main_path}{sub_dir}\\{dir_ext}'
    # os.umask(0)
    print(sub_dir_ext)
    if not os.path.exists(dir_ext):
        os.makedirs(dir_ext, mode=0o777)
    listdir = os.listdir(os.getcwd())
    for i in listdir:
        if checkExtension(i, emote_ext):
            shutil.move(i, f'pic_emote/{i}')
            # break


if __name__ == "__main__":
    main()
