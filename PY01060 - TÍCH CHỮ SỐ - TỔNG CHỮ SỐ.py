from math import *

def solve(s):
    sumEven = 0
    multiOdd = 1
    for i in range(0, len(s)):
        if i % 2 == 1:
            sumEven += int(s[i])
        else:
            if s[i] != '0':
                multiOdd *= int(s[i])
                
    print(multiOdd, sumEven)
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