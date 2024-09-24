from math import *

def gcd (a, b):
    if b == 0: return a
    return gcd(b, a%b)

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1, 1):
        if(n % i == 0): return False
    return True

test = int(input())
while(test > 0):
    test -= 1
    n = int(input())
    cnt = 0
    for x in range(1, n, 1):
        if gcd(x, n) == 1:
            cnt += 1
    
    if isPrime(cnt):
        print("YES")
    else:
        print("NO")
    
