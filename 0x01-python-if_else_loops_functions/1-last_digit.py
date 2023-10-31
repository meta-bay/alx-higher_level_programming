#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numberd = -number % 10
    numberd = -numberd
else:
    numberd = number % 10
if numberd > 5:
    print(f"Last digit of {number} is {numberd} and is greater than 5")
elif numberd == 0:
    print(f"Last digit of {number} is {numberd} and is 0")
elif numberd < 6 and numberd != 0:
    print(f"Last digit of {number} is {numberd} and is less than 6 and not 0")
