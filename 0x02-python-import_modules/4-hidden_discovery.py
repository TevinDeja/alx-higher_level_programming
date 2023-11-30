#!/usr/bin/python3
import importlib.util
import sys

if sys.version_info < (3, 8):
    print("This program requires Python 3.8+")
    sys.exit(1)

spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

names = []
for name in dir(module):
    if not name.startswith('__'):
        names.append(name)

names.sort()

for name in names:
    print(name)
