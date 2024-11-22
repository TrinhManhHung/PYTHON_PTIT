from math import *

test = int(input())
for t in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]: cnt += 1
    print(arr[len(arr) -1] - arr[0] + 1 - cnt)

'''
2
5
4 5 3 8 6
3
2 1 3
'''
