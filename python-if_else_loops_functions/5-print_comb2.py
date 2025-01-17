#!/usr/bin/python3

last_number = ord('c')

for x in range(99):
    if x < 98:
        print("{:02d}" .format(x), end=', ')
    else:
        print(x)
