#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math

    answer = 0
    for n in sys.argv:
        answer += int(n)
        print("{}".format(answer))
