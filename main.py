import random
import os

#this gives a login or register option
#login is stored in usernames.txt and is re-written on subsequent registers
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
            with open('usernames.txt','w') as f:
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
        with open('usernames.txt','r') as f:
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

print(name)

flist = ['salmon', 'trout', 'catfish', 'eel', 'kraken']
money = 0

#this randomly selects a fish from flist and writes it to fish.txt
def cast():
    fish = random.choice(flist)
    print('you caught a ' + fish)
    with open('fish.txt','a') as f:
        f.write(fish+'\n')

#this checks fish.txt for fish and adds to money based on fish name
def sell():
    global money
    with open('fish.txt','r') as f:
        tmoney=0
        for line in f:
            fish = f.readline()
            print(fish)
            if(fish=='salmon\n'):
                money+= 3
                tmoney+= 3
            elif(fish=='trout\n'):
                money+= 5
                tmoney+= 5
            elif(fish=='catfish\n'):
                money+= 10
                tmoney+= 10
            elif(fish=='eel\n'):
                money+= 15
                tmoney+= 15
            elif(fish=='kraken\n'):
                money+= 50
                tmoney+= 50
            else:
                print('error')
        print('you sold all your fish and earned $'+str(tmoney)+'\nyour curent money is $'+str(money))
    with open('fish.txt','w') as f:
        f.write("")
