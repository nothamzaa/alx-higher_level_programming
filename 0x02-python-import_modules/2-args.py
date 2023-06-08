#!/usr/bin/python3
from sys import argv

length = len(argv) - 1
args = argv[1:]

print("{} argument{}{}".format(length, 's' if length != 1 else '', ':' if length > 0 else '.'))

for i, arg in enumerate(args, start=1):
    print("{}: {}".format(i, arg))
