#!/usr/bin/python3
"""Solves the N-queens puzzle"""


import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = 0
try:
    N = int(sys.argv[1])
except:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

solutions = []
col = set()
pos_diag = set()
neg_diag = set()

def solve(r):
    if r == N:
        copy = solutions[:]
        solutions.append(copy)
        return

    for c in range(N):
        if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
            continue

        col.add(c)
        pos_diag.add(r + c)
        neg_diag.add(r - c)
        solutions.append(c)
        solve(r + 1)
        col.remove(c)
        pos_diag.remove(r + c)
        neg_diag.remove(r - c)
        solutions.pop()

solve(0)

for solution in solutions:
    print(solution)
