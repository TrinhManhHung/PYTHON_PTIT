from math import *

while True:
    n = int(input())
    if n == 0:
        break
    nums = []
    for i in range(n):
        x = int(input())
        nums.append(x)
    
    nums.sort()
    if nums[0] == nums[len(nums) - 1]:
        print("BANG NHAU")
    else:
        print(nums[0], nums[len(nums) - 1])

'''
5
1
2
3
4
5
3
001
22
33333333333333333333333333333333333
3
1
1
1
0
'''