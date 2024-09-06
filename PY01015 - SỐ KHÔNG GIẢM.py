from math import *

test = int(input())

while (test != 0):
    test -= 1
    n = int(input())

    check = True
    
    sau = n % 10
    n //= 10
    while (n != 0):
        truoc = n % 10
        if(truoc > sau) :
            check = False
            break
        sau = truoc
        n //= 10

    if (check == True) :
        print("YES")
    else:
        print("NO")
    
'''
2
12345678888888888888889
65645645465754765876857685846
'''