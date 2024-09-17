from math import *

def checkPrime(sum):
    if sum < 2: return False
    for i in range(2, int(sqrt(sum)) + 1, 1):
        if sum % i == 0: return False
    return True


def checkDigit(n) :
    for i in range(0, len(n), 1):
        if i % 2 != int(n[i]) % 2:
            return False
            
    return True

test = int(input())
for i in range(test):
    n = input()
    sumDigit = 0
    for x in n:
        sumDigit += int(x)
    
    if checkPrime(sumDigit) and checkDigit(n):
        print("YES")
    else:
        print("NO")

'''
2
2345678521
1212121212121212121212121
'''