#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argLn = len(sys.argv)
    if argLn == 1:
        print("{} arguments.".format(argLn - 1))
    elif argLn == 2:
        print("{} argument:".format(argLn - 1))
    else:
        print("{} arguments:".format(argLn - 1))
        for n in range(1, argLn):
            print("{}: {}".format(n, sys.argv[n]))
