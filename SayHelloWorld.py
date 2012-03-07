'''
	SayHelloWorld.py
 
	Written by Leezhm on 7th March, 2012.
	
	Copyright (c) leezhm@126.com, All Right Reserved.
 
	For Chapter 2 The Interactive Shell 

	<<Invent Your Own Computer Games with Python>>
 
'''

import os

print('Hello World')

#This Program says hello and asks for your name.
print('Hello' + "World")
print('What is your name ?')
name = input();
print('Nice to meet you, ' + name)

z = ['a', 'b', 'c', 'd']
i = 0
while i < len(z):
    print(i, z[i])
    i += 1
