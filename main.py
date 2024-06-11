#! python3

import sys
import os
import shutil

emote_ext = ['png', 'jpg', 'gif']
rar_ext = ['rar', 'zip', '7z', 'tar', 'exe']

main_path = 'C:\\Users\\$USERNAME\\'

sub_dir = 'Downloads'

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



def main():
    os.chdir(os.path.expandvars(f'{main_path}{sub_dir}'))
    dir_ext = 'pic_emote'
    dir_ext_2 = 'installer'
    sub_dir_ext = f'{main_path}{sub_dir}\\{dir_ext}'
    listdir = os.listdir(os.getcwd())
    if not os.path.exists(dir_ext):
        os.makedirs(dir_ext, mode=0o777)
    if not os.path.exists(dir_ext_2):
        os.makedirs(dir_ext_2, mode=0o777)
    for i in listdir:
        # pic and emote
        sortFile(i, dir_ext, emote_ext)
        # install file
        sortFile(i, dir_ext_2, rar_ext)


if __name__ == "__main__":
    main()
