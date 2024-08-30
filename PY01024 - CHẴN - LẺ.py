from math import *

def solve(n):
    sumOfDigit = 0;

    r = n % 10
    sumOfDigit += n % 10
    n //= 10
    while n != 0 :
        du = n % 10
        sumOfDigit += du
        if abs(du - r) != 2:
            return False;
        r = du
        n //= 10
    
    return True if sumOfDigit % 10 == 0 else False

# Chạy các bộ test
t = int(input())
for _ in range(t):
    n = int(input())
    if solve(n):
        print("YES")
    else :
        print("NO")
