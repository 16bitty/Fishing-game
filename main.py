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

rod = 'basic'
common = ['salmon', 'trout', 'carp', 'tuna', 'boot']
rare = ['eel', 'lobster', 'angelfish', 'squid']
legendary = ['kraken', 'dragon', 'leviathan']
rarity=[common,rare,legendary]
money = 0

#this randomly selects whether to choose from fcommon,frare,or flegendary
#once chosen, it chooses a random item and appends it to fish.txt
def cast():
    global rarity
    if(rod=='basic'):
        frarity=random.choices(rarity, weights=[90,10,0])
    elif(rod=='reinforced'):
        frarity=random.choices(rarity, weights=[49,50,1])
    elif(rod=='platinum'):
        frarity=random.choices(rarity, weights=[10,80,10])
    fish=random.choice(frarity)
    fish=random.choice(fish)
    print('you caught a '+fish)
    with open('fish.txt','a') as f:
        f.write(fish+'\n')

#this checks fish.txt for fish and adds to money based on fish name
def sell():
    global money
    with open('fish.txt','r') as f:
        tmoney=0
        for line in f:
            fish = line.strip()
            if(fish=='salmon' or fish=='trout'):
                money+= 3
                tmoney+= 3
            elif(fish=='carp' or fish=='tuna'):
                money+= 5
                tmoney+= 5
            elif(fish=='eel' or fish=='lobster'):
                money+= 10
                tmoney+= 10
            elif(fish=='angelfish' or fish=='squid'):
                money+= 15
                tmoney+= 15
            elif(fish=='kraken' or fish=='dragon' or fish=='leviathan'):
                money+= 200
                tmoney+= 200
            else:
                pass
        print('you sold all your fish and earned $'+str(tmoney)+'\nyour curent money is $'+str(money))
    with open('fish.txt','w') as f:
        f.write("")

def buy():
    global rod
    global money
    print('there are three rods available for purchase, your current rod is: '+rod)
    print('basic - $20\nreinforced - $100\nplatinum - $1000')
    print('your current money is: $'+str(money))
    choice=input('which rod do you want to buy? enter "none" to exit: ')
    if(choice=='basic' and money<20 or choice=='reinforced' and money<100 or choice=='platinum' and money<1000):
        print("you don't have enough money for that")
    elif(choice=='basic'):
        money-=20
        rod='basic'
        print("your new rod is: "+rod)
    elif(choice=='reinforced'):
        money-=100
        rod='reinforced'
        print("your new rod is: "+rod)
    elif(choice=='platinum'):
        money-=1000
        rod='platinum'
        print("your new rod is: "+rod)
    elif(choice=='none'):
        print('exiting...')
    else:
        print('please input "common","reinforced,"platinum" or "none"')
        buy()
    
