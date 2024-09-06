from math import *

test = int(input())
while test > 0:
    test -= 1

    n = int(input())
    if n % 7 == 0:
        print(n)
    else:
        cnt = 0
        while cnt <= 1000:
            tmp = str(n)[::-1]
            n += int(tmp)
            if(n % 7 == 0):
                print(n)
                break
            cnt += 1
        
        if cnt > 1000:
            print(-1)
