from math import *
from functools import cmp_to_key
from itertools import combinations

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(set(input().split()))
    arr.sort()
    for i in combinations(arr, k):
        print(*i)

'''
6 2
DONG TAY NAM BAC TAY BAC
'''