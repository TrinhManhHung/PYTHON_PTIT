from math import *

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def checkPrime (a):
    if(a <= 1) :
        return False
    for i in range(2, int(sqrt(a)) + 1):
        if(a % i == 0) :
            return False
    return True

test = int(input())
while (test != 0):
    test -= 1
    a, b = map(int, input().split())
    uocChung = gcd(a, b)
    sumDigit = 0
    while uocChung != 0:
        sumDigit += uocChung % 10
        uocChung //= 10

    if (checkPrime(sumDigit) == True) :
        print("YES")
    else:
        print("NO")
    
'''
3
28 42
123 18
550 55
'''