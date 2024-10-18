from math import *

test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    nums = {}
    for i in range(n):
        if arr[i] not in nums:
            nums[arr[i]] = 1
        else:
            nums[arr[i]] += 1

    a = list(nums.keys())
    for key in a:
        if nums[key] % 2 != 0:
            print(key)
            break
'''
2
7
1 2 3 2 3 1 3
5
1 1 3 3 2
'''