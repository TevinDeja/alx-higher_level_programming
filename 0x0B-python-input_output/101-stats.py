#!/usr/bin/python3
"""Reads from standard input and computes metrics"""
import sys

total_size = 0
status_codes = {}

for line_num, line in enumerate(sys.stdin, 1):
    line = line.split()
    total_size += int(line[-1])

    status_code = line[-2]
    if status_code in status_codes:
        status_codes[status_code] += 1
    else:
        status_codes[status_code] = 1

    if line_num % 10 == 0:
        print("File size: {}".format(total_size))
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print("{}: {}".format(code, status_codes[code]))
