from math import *

n = int(input())
arr = []
for i in range(n):
    tam = list(map(int, input().split()))
    arr.append(tam)

k = int(input())
sumUp = 0
sumDown = 0
for i in range(n):
    for j in range(n):
        if j < (n-i-1):
            sumUp += arr[i][j]
        elif j > (n-i-1):
            sumDown += arr[i][j]

res = abs(sumUp - sumDown)
if res <= k:
    print("YES")
else:
    print("NO")
print(res)
'''
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
'''