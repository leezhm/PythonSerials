'''
	GuessNumbers.py
	
	Written by Leezhm on 7th March, 2012.
	
	Copyright (c) Leezhm@126.com. All Right Reserved.
	
	For Chapter 4 Guess the Number
	
	<<Invent Your Own Computer Games with Python>>
'''

import random

guessesToken = 0

print("Hello! What is your name ?")
name = input()

number = random.randint(1, 30)
print('Well, ' + name + ', I am thinking of a number between 1 and 30.')

while guessesToken < 6 :
	print('Token a guess.')
	guess = int(input())
	
	guessesToken += 1
	
	if guess < number :
		print('Your guess is too low.')
	elif guess > number :
		print("Your guess is too high.")
	else :
		print('Congrulation !!! ' + name + "! You guessed my number in " +
		       str(guessesToken) + ' guesses!')
		break
	
if guess != number :
        print('Nope. The number i was thinking of was ' + str(number))
		
