#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1
    compute = 1
    if b > 0:
        for i in range(b):
            compute *= a
    if b < 0:
        for i in range(abs(b)):
            compute *= a
        compute = 1 / compute
    return compute

