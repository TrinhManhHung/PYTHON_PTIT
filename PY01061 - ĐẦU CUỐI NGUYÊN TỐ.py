from math import *

def checkPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

test = int(input())
while test > 0:
    test -= 1
    s = input()
    dau = int(s[:3])
    cuoi = int(s[len(s) - 3:])
#    print(dau, cuoi)
    if checkPrime(dau) and checkPrime(cuoi):
        print("YES")
    else:
        print("NO")

'''
3
12743
7337
12345678901234
'''
