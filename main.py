import random
import time
import sys

name = "default"
def setup():
    global name
    ans=input('do you want to login or register?: ')
    if(ans=='register'):
        username = str(input('username: '))
        password = str(input('password: '))
        login = (username+password)
        confirm = str(input('this will overwrite any previous data, are you sure?(yes/no): '))
        if(confirm=='yes'):
            with open('usernames.txt', 'w') as f:
                f.write(login)
                name = login
        elif(confirm=='no'):
            print('returning to setup')
            setup()
        else:
            print('unexpected input detected, returning to setup')
            setup()
    elif(ans=='login'):
        username = str(input('username: '))
        password = str(input('password: '))
        login = (username+password)
        with open('usernames.txt', 'r') as f:
            for line in f:
                if line == login:
                    print('you have logged in')
                    a = True
                    name = line
                    break
                else:
                    a = False
                    pass
            if(a==False):
                print('your username and/or password was incorrect')
                setup()
    else:
        print('please either input "login" or "register"')
        setup()
setup()
print(name)
