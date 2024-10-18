from math import *

def checkPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))

b = []
for x in a:
    if x not in b:
        b.append(x)

m = len(b)
allOfSum = sum(b)
curSum = 0
checkExist = False
for i in range(0, m):
    curSum += b[i]
    if checkPrime(curSum) and checkPrime(allOfSum - curSum):
        print(i)
        checkExist = True
        break

if checkExist == False: print("NOT FOUND")


