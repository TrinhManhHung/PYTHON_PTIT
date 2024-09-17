from math import *

def checkPrime(sum):
    if sum < 2: return False
    for i in range(2, int(sqrt(sum)) + 1, 1):
        if sum % i == 0: return False
    return True

def solve(s) :
    for i in range(0, len(s)):
        if (checkPrime(i) and checkPrime(int(s[i])) == False) or (checkPrime(i) == False and checkPrime(int(s[i]))):
            return False
    
    return True
    
test = int(input())
for i in range(test):
    s = input()
    if solve(s): print("YES")
    else: print("NO")

'''
2
14239567
2314514535353
'''