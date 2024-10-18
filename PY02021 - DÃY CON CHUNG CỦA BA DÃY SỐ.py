from math import *
from collections import *

test = int(input())
while test > 0:
    test -= 1
    n, m, p = map(int, input().split())
    a = Counter(list(map(int, input().split())))
    b = Counter(list(map(int, input().split())))
    c = Counter(list(map(int, input().split())))

    nums = list((a & b & c).elements())
#    nums = list((nums & c).elements())

    if len(nums) == 0:
        print("NO")
    else:
        nums.sort()
        for x in nums:
            print(x, end = ' ')
        print()



