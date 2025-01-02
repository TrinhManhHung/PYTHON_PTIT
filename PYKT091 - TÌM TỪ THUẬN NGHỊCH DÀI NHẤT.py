from math import *
from functools import cmp_to_key
from itertools import combinations

def isTN(s):
    n = len(s)
    for i in range(0, int(n/2)):
        if s[i] != s[n-i-1]: return False
    return True
if __name__ == '__main__':
    f = open('VANBAN.in', 'r')
    arr = []
    tanSuat = dict()
    max_len = 0
    for x in f:
        tmp = x.strip().split()
        for y in tmp:
            if isTN(y):
                max_len = max(max_len, len(y))
                arr.append(y)
                tanSuat[y] = tanSuat.get(y, 0) + 1

    for x in arr:
        if len(x) == max_len and tanSuat[x] != 0:
            print(x, tanSuat[x])
            tanSuat[x] = 0