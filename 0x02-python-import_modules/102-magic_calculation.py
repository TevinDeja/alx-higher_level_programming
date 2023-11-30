#!/usr/bin/python3
def magic_calculation(x, y):
    from magic_calculation_102 import add, sub
    if x < y:
        result = add(x, y)
        for n in range(4, 6):
            result = add(result, n)
            return result
    else:
        return sub(x, y)
