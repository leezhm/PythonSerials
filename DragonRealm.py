'''
#	DragonRealm.py
#	
#	Written by leezhm on 10th March, 2012.
#
#	Copyright (c) leezhm@126.com, All Right Reserved.
#
#	For Chapter 4 Dragon Realm
#
#	<<Invent Your Own Computer Games with Python>>
#
'''

import random
import time


print('For Chapter 6 Dragon Realm')

def displayInformation() :
    print('You are on a planet full of dragons.In front of you, you can see two caves.')
    print('In one cave, the dragon is friendly and will share his treasures with you.')
    print('The other dragon is greedy and hungry, and will eat you on sight.\n')

def chooseCave() :
    cave = 0
    while '1' != cave and '2' != cave :
        print('Which cave will you go into(1 or 2)?')
        cave = input()

    return cave

def checkCave(choose) :
    print('You approach the cave ...')
    time.sleep(2)
    print('It is dark and spooky ...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He open his jaws and ...\n')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)
    if str(friendlyCave) == choose :
        print('Give you his treasures !')
    else :
        print('Gobbles you down in one bite!')

playAgain = 'yes'

while 'yes' == playAgain or 'y' == playAgain :
    displayInformation()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again?(yes or no)')
    playAgain = input()


