from math import *

def solve(s):
    sumEven = 0
    multiOdd = 1
    checkAllZero = True
    for i in range(0, len(s)):
        if i % 2 == 0:
            sumEven += int(s[i])
        else:
            if s[i] != '0':
                checkAllZero = False
                multiOdd *= int(s[i])
                
    if checkAllZero:
        print(sumEven, 0)
    else :
        print(sumEven, multiOdd)
test = int(input())
for i in range(test):
    s = input()
    solve(s)

'''
3
12345678
20000
22334455667788
'''