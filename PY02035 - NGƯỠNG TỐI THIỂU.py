from math import *

s = input()
k = int(input())
nums = {}

while len(s) >= 2:
    cut = s[:2]
    nums[cut] = nums.get(cut, 0) + 1
    s = s[2:]

checkExist = False

for keys, values in sorted(nums.items()):
    if values >= k:
        print(keys, values)
        checkExist = True
if(checkExist == False): print("NOT FOUND")




