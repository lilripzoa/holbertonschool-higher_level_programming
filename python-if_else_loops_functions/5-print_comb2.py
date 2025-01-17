#!/usr/bin/python3

last_number = ord('c')

for x in range(100):
    if x < 99:
        print("{:02d}" .format(x), end=', ')
    else:
        print(x)
