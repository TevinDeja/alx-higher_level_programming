#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for n in range(x):
            print(my_list[n], end='')
            counter += 1
        print()
    except IndexError:
        pass
    return counter
