import random
import time
import sys

def setup():
    ans=input('do you want to login or register? ')
    if(ans=='register'):
        username = str(input('username: '))
        password = str(input('password: '))
        login = (username+password)
        with open('usernames.txt', 'w') as f:
            f.write(login)
    elif(ans=='login'):
        username = str(input('username: '))
        password = str(input('password: '))
        login = (username+password)
        with open('usernames.txt', 'r') as f:
            for line in f:
                if line == login:
                    print('you have logged in')
                    a = True
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
