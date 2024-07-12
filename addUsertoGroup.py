#!/usr/bin/python3
import os
import userCreate 

def addUserGroup(user):

    if userCreate.checkUser(user):
        print(f"adding {user} to {group}")
        os.system(f"usermod -G {group} {user}")
    
    else:
        print(f'{user} does not exist !!!')
        if userCreate.createUser(user):
            addUserGroup(user)

        

group = input("Type the group you want to add the user(s)\nGroup Name :")
if userCreate.checkGroup(group):
    users = input("Type the user(s) you want to add to the existing Group\nIf there are more than one user then use a comma ',' to separate it.\ne.g user1,user2,user3\nUser(s) : ").split(',')
    
    for user in users:
        addUserGroup(user)

else:
    userCreate.createGroup(group)


