from math import *

test = int(input())

while(test > 0):
    test -= 1
    s = input()
    res = ""
    sum = 0
    for x in s:
        if(x >= '0' and x <= '9'):
            sum += int(x)
        else:
            res += x
    
    res = ''.join(sorted(res)) + str(sum)
    print(res)
