from math import *

def checkPrime(sum):
    if sum < 2: return False
    for i in range(2, int(sqrt(sum)) + 1, 1):
        if sum % i == 0: return False
    return True


test = int(input())
for i in range(test):
    s = input()
    n = int(s[len(s)-4:])
#    print(n)
    if checkPrime(n): print("YES")
    else: print("NO")

'''
3
12234323130097
3443354654654654461123
43543543434554659999
'''