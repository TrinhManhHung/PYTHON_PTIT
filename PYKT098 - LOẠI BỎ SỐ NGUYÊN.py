from math import *
from functools import cmp_to_key
from itertools import combinations

if __name__ == '__main__':
    max_int = 2**31 - 1
    f = open('DATA.in', 'r')
    arr = []
    for line in f:
        tmp = line.strip().split()
        for x in tmp:
            if not (x.isdigit() and int(x) <= max_int):
                arr.append(x)
    arr.sort()
    for x in arr:
        print(x, end = ' ')

