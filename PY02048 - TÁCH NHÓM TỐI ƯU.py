from math import *

n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

if n == 0: print(0)
else:
    cnt = 1
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > k:
            cnt += 1
    print(cnt)
'''
7 1
2 6 1 7 3 4 9
'''
