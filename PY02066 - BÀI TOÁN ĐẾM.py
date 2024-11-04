from math import *

n = int(input())
nums = []
while len(nums) != n:
    tmp = list(map(int, input().split()))
    nums.extend(tmp)

maxElement = max(nums)
miss = []
idx = 1
while idx <= maxElement:
    if idx not in nums:
        miss.append(idx)
    idx += 1

if len(miss) == 0:
    print("Excellent!")
else:
    for x in miss:
        print(x)
'''
'''