"""Flow control statemnts, etc."""

# spam = 0

# while spam < 7:
#     print(str(spam) + '. you have entered the right integer')
#     spam = spam + 1

# if spam < 5:
#     print('Hello, world.')
#     spam = spam + 1

# name = ''
# while name != 'your name':
#     print('please type your name.')
#     name = input()
# print('Thank you')

# while True:
#     print('Please type your name:')
#     name = input()
#     if name == 'your name':
#         break

# print('Thank you!')

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

"""TRUTHY AND FALSEY VALUES"""

# name = ''
# while not name:
#     print('Enter your name:')
#     name = input()

# print('How many guests will you have?')
# numOfGuests = int(input())

# if numOfGuests:
#     print('Be sure to have enough room for all your guests.')
# print('Done')


"""for loops and range function"""

# print('My name is ')
# for i in range(5):
#     print('Jimmy Five Times (' + str(i) + ')')
    
"""the Karl Fredrich Gauss Solution"""
# total = 0
# for num in range(101):
#     total = total + num
# print(total)

"""An equivalant while loop"""
# print('my name is: ')
# i = 0

# while i < 5:
#     print('Jimmy  five times (' + str(i) +  ')')
#     i = i + 1

"""Another example to add numbers from 0 to 100"""

# total = 0
# for num in range(101):
#     total = total + num

# print(total)

"""Five times code using a while loop"""

# print('My name is')
# i = 0

# while i < 5:
#     print('Jimmy Five times (' + str(i) + ')')
#     i = i + 1

"""starting, stopping and stepping"""

# for i in range(12, 16):
#     print(i)

"""calling the range function to count with interals of two"""

# for i in range(0, 20, 2):
#     print(i)

"""more with the for loop"""

# for i in range(5, -1, -1):
#     print(i)

"""ending programs abrubtly using the sys() function."""

import sys

while True:
    print('Type exit to exit.')
    response  = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')


name = 'Osasu'

if name == 'Osasu':
  print('Hello, Osasu')
