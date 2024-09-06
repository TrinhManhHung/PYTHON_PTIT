from math import *

def check (s):
    if(len(s) < 3): return False
    check = False
    for i in range(0, len(s)-1):
        if(s[i] == s[i+1]):
            return False
        if(s[i] > s[i+1]):
            check = True
        if (check == True):
            if(s[i] < s[i+1]):
                return False

    return True

test = int(input())
while test > 0:
    test -= 1
    n = input()
    if(check(n)) : print("YES")
    else : print("NO")
