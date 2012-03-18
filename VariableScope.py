'''
#   VariableScope.py
#
#   Written by leezhm on 13th March, 2012.
#
#   Copyright (C) leezhm(c)126.com. All Right Reserved.
#
#   For Chapter 6 Dragon Realm
#
#   <<Invent Your Own Computer Games with Python>>
'''

print('Why not ?')

print(True and not False)

# A global variable named "spam"
spam = 1208

# This block doesn't run until funky() is called.
def funky() :
    # We read the global variable's value:
    # print(spam)

    # We create a local variable named "spam"
    # instead of changing the value of the global variable "spam"
    spam = 302

    # The name "spam" now refers to the local variable only
    # for the rest of this function:
    print(spam)

# Call the function funky():
funky()

# The global variable was not changed in funky():
print(spam)

# Function with parameters
def sayHello(name) :
    print('Hello, ' + name)

print('Say hello to Alice.')
fizzy = 'Alice'
sayHello(fizzy)
print('Do not forget to say hello to Bob.')
sayHello('Bob')

sayHello('Lee')

def spam(myName) :
    print('Hello, ' + myName)
    myName = 'Waffles'
    print('Your new name is ' + myName)

myName = 'Albert'
spam(myName)
print('Howdy, ' + myName)