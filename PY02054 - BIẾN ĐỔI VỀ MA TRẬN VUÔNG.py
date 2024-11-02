from math import *

n, m = map(int, input().split())
arr = []

for N in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)

if n == m:
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end = " ")
        print()
else:
    if n > m:
        sz = n - m
        for i in range(n):
            if i % 2 == 0 and sz > 0:
                sz -=1
            else:    
                for j in range(m):
                    print(arr[i][j], end = " ")
                print()


    else:
        sz = m - n
        cols = []
        idx = 1
        while sz > 0:
            cols.append(idx)
            idx += 2
            sz -= 1
        for i in range(n):
            for j in range(m):       
                if j not in cols:
                    print(arr[i][j], end = " ")
            print() 

'''
4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7
'''