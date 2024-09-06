from math import *

test = int(input())

while (test != 0):
    test -= 1
    n = int(input())
    check = False
    if (n % 10 == 6 and (n//10) % 10 == 8):
        check = True
    if (check == True) :
        print("YES")
    else:
        print("NO")
    
