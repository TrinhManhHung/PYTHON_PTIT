from math import *

n = int(input())

arr = []
for i in range(n):
    tam = list(map(int, input().split()))
    arr.append(tam)

if n == 2:
    print(int(arr[0][1] / 2), int(arr[0][1] / 2))
else:
    tmp = [] #tmp[i] = a[i] - a[i-1]
    tmp.append(0)
    for i in range(1, n-1):
        tmp.append(arr[i][n-1] - arr[i-1][n-1])
    tmp.append(arr[n-1][0] - arr[n-2][0])

    a = []
    a.append(int((arr[0][1] - tmp[1]) / 2))
    for i in range(1, n):
        nexte = a[len(a)-1] + tmp[i]
        a.append(nexte)
    
    for i in a: print(i, end = " ")

'''
4
0 3 6 7
3 0 5 6
6 5 0 9
7 6 9 0
'''
