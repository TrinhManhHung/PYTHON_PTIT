from math import *
from functools import cmp_to_key
from itertools import permutations

if __name__ == '__main__':
    #help(permutations)
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = ''
        for i in range(1, n+1):
            s += str(i)

        arr = sorted(permutations(s), reverse = True)
        print(len(arr))
        for x in arr:
            print(''.join(x), end = ' ')
        print()