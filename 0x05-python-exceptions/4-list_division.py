#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    for n in range(list_length):
        try:
            res = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        else:
            new_list[n] = res
    return new_list
