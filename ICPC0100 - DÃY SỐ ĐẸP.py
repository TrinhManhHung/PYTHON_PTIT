from math import *

t = int(input())
for T in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(0, len(arr)-1):
        x = min(arr[i], arr[i+1])
        y = max(arr[i], arr[i+1])
        cnt = 0
        while x * (2**cnt) < y: cnt+=1
        res += max(0, cnt - 1)
    print(res)
'''
6
4
4 2 10 1
2
1 3
2
6 1
3
1 4 2
5
1 2 3 4 3
12
4 31 25 50 30 20 34 46 42 16 15 16
'''
