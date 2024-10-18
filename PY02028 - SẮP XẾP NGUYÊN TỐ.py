from math import *

def checkPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))

primeList = []
for x in arr:
    if checkPrime(x):
        primeList.append(x)

primeList.sort()
for x in arr:
    if checkPrime(x):
        print(primeList[0], end = ' ')
        primeList.pop(0)
    else:
        print(x, end = ' ')
