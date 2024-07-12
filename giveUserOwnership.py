#!/usr/bin/python3

import userCreate  
import checkFile 
import os

user = input("Enter the user name you want to grant the permission :")
directory = input("Enter the directory you want to grant the user ownership :")

def pathOwner(user,path):
    if checkFile.pathChecker(path):
        os.system(f'chown {user}:{user} {path}')
    else:
        responds=input("Do you want to create the path ?\nReply Y for yes or N for no :").upper()
        if responds == "Y":
            doc = input("Enter f for file or d for directory :").lower()
            if doc=='f':
                checkFile.createFile(path)
            else :
                checkFile.createFolder(path)
            print(f"{path} created !")
            os.system(f'chown {user}:{user} {path}')



if userCreate.checkUser(user):
    pathOwner(user,directory)
else :
    if userCreate.createUser(user):
        pathOwner(user,directory)
    else :
        print("Bye !!!")
