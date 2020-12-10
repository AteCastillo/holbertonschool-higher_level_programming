#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = sys.argv[2]

    if c == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif c == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif c == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif c == '/':
        print('{} / {} = {}'.format(a, b, div(a, b)))
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
