from math import *

#Tinh UCLN
def gcd (a, b):
    if(b == 0):
        return a
    return gcd (b, a%b)
#main
#input
test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    #Tim so dao cua n
    revn = 0
    tmp = n
    while tmp != 0:
        revn = revn * 10 + tmp % 10
        tmp //= 10
    #output
    if gcd(n, revn) == 1:
        print("YES")
    else :
        print("NO")

