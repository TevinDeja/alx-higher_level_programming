#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    answer = 0
    for n in range(len(sys.argv) - 1):
        answer += int(sys.argv[n + 1])
    print("{}".format(answer))
