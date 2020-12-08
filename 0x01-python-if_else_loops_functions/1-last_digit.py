#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdi = (number * -1) % 10
    lastdi = (lastdi * -1)
else:
    lastdi = number % 10

if lastdi > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, lastdi))

elif lastdi == 0:
    print("Last digit of {} is {} and is 0".format(number, lastdi))

else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, lastdi))
