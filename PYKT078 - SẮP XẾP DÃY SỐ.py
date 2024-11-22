from math import *

test = int(input())
for t in range(test):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    maxVal = max(arr)
    for i in range(0, n):
        if arr[i] == maxVal:
            arr.insert(i, m)
            break
    
    for i in range(0, n+1):
        if arr[i] < 0: print(arr[i], end = " ")
    for i in range(0, n+1):
        if arr[i] >= 0: print(arr[i], end = " ")  
    print()

'''
1
5 3
-1 2 3 4 -1
'''
