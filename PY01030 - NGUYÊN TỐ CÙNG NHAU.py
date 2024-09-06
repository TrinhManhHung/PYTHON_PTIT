from math import *

def gcd (a, b):
    if(b == 0):
        return a
    return gcd (b, a%b)
#input
n, k = map(int, input().split())
#tim cac so nt cung nhau va in ra
cnt = 0
for i in range(int(pow(10, k-1)), int(pow(10, k))):
    if gcd(n, i) == 1:
        cnt += 1
        print(i, end = ' ')
        if cnt % 10 == 0:
            print()