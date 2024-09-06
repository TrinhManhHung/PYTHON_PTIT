from math import *

test = int(input())

while (test != 0):
    test -= 1
    n = int(input())
    check = True;
    while n != 0 :
        r = n % 10
        if(r != 4 and r != 7):
            check = False
            break
        n //= 10

    if (check == True) :
        print("YES")
    else:
        print("NO")
    
