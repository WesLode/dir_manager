import sys
import os
import shutil

main_path = 'C:\\Users\\$USERNAME\\'
main_path = 'C:\\Users\\$USERNAME\\'
sub_dir = 'Downloads'
sorted_dir = ['pic_emote','installer']

def listDirectories():
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x)

def reset():
    for i in sorted_dir:
        os.chdir(os.path.expandvars(f'{main_path}{sub_dir}\\{i}'))
        listdir = os.listdir(os.getcwd())
        for i in listdir:
            shutil.move(i, f'..\\{i}')
            # print(i)


if __name__ == "__main__":
    reset()