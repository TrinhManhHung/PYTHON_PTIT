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
    size = len(s)
    primeDigit = 0
    for x in s:
        if(x == '2' or x == '3' or x == '5' or x == '7'):
            primeDigit += 1
    
    if primeDigit > (size - primeDigit) and checkPrime(size):
        print("YES")
    else:
        print("NO")

'''
3
1234567
22334455667
23400300489898989
'''
