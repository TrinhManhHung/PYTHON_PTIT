# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

from math import *

while True:
    nums = list(map(int, input().split()))
    cnt = 0
    if nums[0] == nums[1] and nums[1] == nums[2] and nums[2] == nums[3] and nums[0] == 0:
            break
    else:
        while True:
            if nums[0] == nums[1] and nums[1] == nums[2] and nums[2] == nums[3]:
                break
            tam = []
            cnt += 1
            for i in range(0, 4):
                tam.append(abs(nums[i%4] - nums[(i+1) % 4]))
            nums = tam
        print(cnt)
        
        
    
    

