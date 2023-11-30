#!/usr/bin/python3
import custom_module

def my_calculation(x, y):

    from my_calculation_utilities import multiply, divide

    if x > y:

        z = multiply(x, y)

        for i in range(2, 4):

            z = multiply(z, i)

        return z

    else:

        return divide(x, y)
