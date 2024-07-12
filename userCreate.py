#!/usr/bin/python3

import os

def checkUser(user):
     return os.system(f'id {user}') == 0

def createUser(user):
    u_option = input(f"Do you want to create a new user called {user}?\nType Y for Yes or N for NO\nNew User:").upper()
    if u_option == "Y":
        print(f"Creating User ...")
        os.system(f'useradd {user}')
        print(f"{user} has been added !!!\n")
        return True
    elif u_option == "N":
        print(f"{user} not added !")
        return False
    else:
        print("Wrong input !!!")
        return False

def checkGroup(group):            
    return os.system(f'grep {group} /etc/group') == 0

def createGroup(group):    
    g_option=input(f"Do you want to create a new group called {group}?\nType Y for Yes or N for NO\nNew Group:").upper()
    if g_option == "Y":
        print("Creating Group")
        os.system(f"groupadd {group}")
        print(f"{group} has been added !!!")
        return True
    elif g_option == "N":
        print(f"{group} not added !")
        return False
    else:
        print("Wrong Input !!!")
        return False

def main():
    command = input("What do you want to do ?\nFor creating or searching for a user type U\nFor searching for a Group type G \nResponds :").upper()

    if command == 'U':
    
        users = input("Enter User(s)\nIf you have more than one user, use a comma to seprate the names\ne.g devops,jekins,coop\nUser(s):").split(',')
        for user in users:    
            if checkUser(user):
                print(f'{user} exists !')
            else:
                print(f'{user} does not exist !')
                createUser(user)

    elif command == "G":
        groups = input("Enter Group(s)\nIf you have more than one group, use a comma to seprate the names\ne.g devops,jekins,coop\nGroup(s):").split(',')
        for group in groups:
            if checkGroup(group):
                print(f'{group} exists !')
            else:
                print(f'{group} does not exist !')
                createGroup(group)       

    else:
        print("Wrong Input !!!")

