from math import *

def checkTN(n) :
    s = str(n)
    if(len(s) == 1): return False
    s1 = s[::-1]
    return s == s1

test = int(input())
for i in range(test):
    n = input()
    sumDigit = 0
    for x in n:
        if x != '0':
            sumDigit += int(x)
    
    if(checkTN(sumDigit)): print("YES")
    else: print("NO")
    
    