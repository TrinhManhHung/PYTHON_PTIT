from math import *

n, m = map(int, input().split())
arr = []
maxNum = 0
minNum = 10005
for N in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)
    maxNum = max(maxNum, max(nums))
    minNum = min(minNum, min(nums))


luckyNum = int(maxNum - minNum)

found = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == luckyNum:
            if found == False:
                print(luckyNum)
                found = True
            print(f"Vi tri [{i}][{j}]")

if not found: print("NOT FOUND")
'''
6 4
23 21 77 10
13 13 22 14
28 77 28 23
29 77 11 77
16 51 24 21
13 25 77 77
'''