from math import *

def PhanTich(n):
    m = n
    res = "1 * "
    
    for i in range(2, int(sqrt(m) + 1), 1):
        if m % i == 0:
            cnt = 0
            while m % i == 0:
                cnt += 1
                m //= i
            res += str(i) + "^" + str(cnt) + " * "
    
    if m > 1: res += str(m) + "^1 * "
    return res[:-3]
    
test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    print(PhanTich(n))