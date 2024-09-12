from math import *

def checkPrime(n) :
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True

test = int(input())
while test != 0:
    test -= 1
    s = int(input())
    n = 0
    lap = 0
    while lap < 4:
        n = (s % 10) * (10**lap) + n
        s //= 10
        lap += 1
    
    if checkPrime(n):
        print("YES")
    else :
        print("NO")

'''
3
12234323130097
3443354654654654461123
43543543434554659999

YES
YES
NO
'''