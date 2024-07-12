#!/usr/bin/python3
import os

def pathChecker(path):

    if os.path.isdir(path):
        print(f"{path} exits and it is a directory !")
        return True
    elif os.path.isfile(path):
        print(f"{path} exits and it is a file !")
        return True
    else:
        print("Path not found !!!")
        return False

def createFile(path):

    result = path.split("/")
    file_name = result[-1]
    folder = path[:-len(file_name)]
    os.system(f'mkdir -p {folder}')
    os.system(f'touch {path}')

def createFolder(path):
    os.system(f'mkdir -p {path}')
def main():
    path = input("Enter the Path of the file or directory You are looking for :")
    if not pathChecker(path):
        doc = input("Enter f for file or d for directory :").lower()
        if doc=='f':
            createFile(path)
        else :
            createFolder(path)
        print(f"{path} created !")


