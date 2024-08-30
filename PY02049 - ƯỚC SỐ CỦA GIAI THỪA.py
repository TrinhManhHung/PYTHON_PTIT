from math import *

t = int(input());
while t > 0 :
        n, p = map(int, input().split());
        cnt = 0;
        while n != 0:
                cnt += n // p
                n //= p
        print(cnt)
        t -= 1

