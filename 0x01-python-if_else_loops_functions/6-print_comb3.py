#!/usr/bin/python3
for num in range(9):
    for dgt in range(num + 1, 10):
        if num * 10 + dgt < 89:
            print("{:d}{:d}".format(num, dgt), end=", ")
print("{:d}".format(89))
