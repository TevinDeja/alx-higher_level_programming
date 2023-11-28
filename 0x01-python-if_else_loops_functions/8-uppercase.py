#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if ord("a") <= ord(n) <= ord("z"):
            n = chr(ord(n) - 32)
        print("{:s}".format(n), end="")
    print()
