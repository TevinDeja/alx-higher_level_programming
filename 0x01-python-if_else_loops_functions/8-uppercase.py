#!/usr/bin/env python3
def uppercase(str):
    print("{}".format(str[0].upper()), end="")
    for c in str[1:]:
        if ord('a') <= ord(c) <= ord('z'):
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print("")
