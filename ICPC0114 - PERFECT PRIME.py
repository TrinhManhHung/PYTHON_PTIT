from math import *

def nt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#check n va n dao la so nt
def check1(n):
    m = int(str(n)[::-1])
    return nt(n) and nt(m)

#check tong cs va cs n la so nt
def check2(n):
    sumDigit = 0
    while n != 0:
        du = n % 10
        if du != 2 and du != 3 and du != 5 and du != 7:
            return False
        sumDigit += du
        n //= 10
    return nt(sumDigit)

test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    if check1(n) and check2(n):
        print("Yes")
    else:
        print("No")
