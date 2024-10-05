from math import *

def giaiThua(n):
    if n < 2: return 1
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def checkKrish(n):
    s = str(n)
    sum = 0
    for i in range(0, len(s)):
        sum += giaiThua(int(s[i]))
    return n == sum

test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    if checkKrish(n):
        print("Yes")
    else:
        print("No")
