#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print("%d is positive" % number)
if number == 0:
    print("%d is zero" % number)
if number < 0:
    print("%d is negative" % number)
