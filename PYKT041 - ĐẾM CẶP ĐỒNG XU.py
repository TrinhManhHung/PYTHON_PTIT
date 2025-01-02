from math import *
from functools import cmp_to_key

if __name__ == '__main__':
    n = int(input())
    matrix = []
    arr = []
    for i in range(n):
        s = input().strip()
        row = list(s)
        matrix.append(row)
        arr.append(s.count('C'))

    for j in range(n):
        cnt = 0
        for i in range(n):
            if matrix[i][j] == 'C': cnt += 1
        arr.append(cnt)

    res = 0
    for i in range(len(arr)):
        if(arr[i] >= 2):
            res += comb(arr[i], 2)

    print(res)

'''
4
CC..
C..C
.CC.
.CC.
'''