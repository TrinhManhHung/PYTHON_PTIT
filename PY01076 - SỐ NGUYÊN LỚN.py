from math import *

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

test = int(input())
while test > 0:
    test -= 1
    a = int(input())
    b = int(input())
    print(gcd(a, b))


'''
1
1221
1234567891011121314151617181920212223242526272829
'''
