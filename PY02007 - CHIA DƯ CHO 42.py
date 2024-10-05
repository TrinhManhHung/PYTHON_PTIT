from math import *
nums = []
while len(nums) < 10:
    nums.extend(map(int, input().split()))


arr = [0] * 42
for num in nums:
    arr[num % 42] = 1

cnt = 0
for i in range(0, 42):
    if arr[i] == 1:
        cnt += 1
print(cnt)

'''
1 2 3 4 5 6  7 8  9 10

42 84 252 420 840
126 42 84 420 126


39 40 41 42 43 44 82
83 84 85
'''
