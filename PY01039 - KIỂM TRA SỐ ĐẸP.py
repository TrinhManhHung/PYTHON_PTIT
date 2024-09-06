from math import *

def check (n):
    digit1 = n % 10
    n //= 10
    digit2 = n % 10
    n //= 10
    cnt = 0
    while n != 0:
        cnt += 1
        if (cnt % 2 == 1) and (n % 10 != digit1):
            return False
        if (cnt % 2 == 0) and (n % 10 != digit2):
            return False
        n //= 10            
    return True

test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    if(check(n)) : print("YES")
    else : print("NO")
