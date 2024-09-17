from math import *

def checkPrime(n) :
    if(n < 2): return False
    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0): return False
    return True

test = int(input())
for i in range(test):
    n = input()
    res = 0
    for x in n:
        if x != '0':
            res += int(x)
    
    if(checkPrime(res)): print("YES")
    else: print("NO")