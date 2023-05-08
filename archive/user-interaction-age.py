from __future__ import print_function
import random
import sys
import os


name = raw_input('Please tell me your name: ')
rawAge = raw_input('Please tell me your age: ')
age = int(rawAge)

if age >= 21:
	print(name, 'you are allowed in!')
	print('What would you like to drink?')
elif age >= 18:
	print('You are allowed in.')
	print('But you are not allowed to drink, please feel free to dance.')
else:
	print('Unforunately', name, 'you are not allowed in.')

