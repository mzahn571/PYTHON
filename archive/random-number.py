# import the random module to randomize numbers

import random


roll = "roLL the dice and take your chances\n"
print roll

print "If you were angry..you would say it like this..\n"
angry = roll.upper()
print angry

print "If you were calmer..you would say it like this..\n"
calmer = roll.lower()
print calmer

raw_input("Press Enter to roll the dice!")

die1 = random.randrange(6) + 1
die2 = random.randrange(6) + 1

print die1
print die2

total = die1 + die2

if total == 2:
	print "snakeeyes!!!!"
	
print "You successully rolled a: ", total 
