from math import *
from functools import cmp_to_key
from itertools import combinations
arr = []
res = []
n = 4
def Try(i, cursum, curs):
    for j in range(i, 0, -1):
        tmp = curs.copy()
        tmp.append(j)
        if cursum + j == n:
            res.append(tmp)
        if cursum < n:

            Try(j, cursum + j, tmp)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        res.clear()
        tmp = []
        Try(n, 0, tmp)
        print(len(res))
        for x in res:
            tmp = ' '.join(str(i) for i in x)
            print(f'({tmp})', end = ' ')
        print()

'''
(4) (3 1) (2 2) (2 1 1) (1 1 1 1)
(4) (3 1) (2 2) (2 1 1) (1 1 1 1) 

(5) (4 1) (3 2) (3 1 1) (2 2 1) (2 1 1 1) (1 1 1 1 1) 
(5) (4 1) (3 2) (3 1 1) (2 2 1) (2 1 1 1) (1 1 1 1 1)
'''