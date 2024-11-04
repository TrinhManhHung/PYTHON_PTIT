from math import *

n = int(input())
a = list(map(int, input().split()))

res = 20000000
num = -1
for i in range(0, n):
    cost = 0
    for j in range(0, n):
        cost += abs(a[j] - a[i])
    if cost < res:
        res = cost
        num = a[i]

print(res, num)