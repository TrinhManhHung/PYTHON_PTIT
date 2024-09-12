from math import *

def checkPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: 
            return False
    return True

test = int(input())

while test > 0:
    s = input()
    cntPrime = 0
    for word in s:
        if(word == '2' or word == '3' or word == '5' or word == '7'):
            cntPrime += 1
    if checkPrime(len(s)) == True and cntPrime > (len(s) - cntPrime):
        print("YES")
    else :
        print("NO")
    test -= 1