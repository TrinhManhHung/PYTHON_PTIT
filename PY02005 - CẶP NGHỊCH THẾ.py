from math import *

n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(0, n - 1):
    for j in range(i+1, n):
        if(arr[i] > arr[j]):
            ans += 1

print(ans)

'''

'''
