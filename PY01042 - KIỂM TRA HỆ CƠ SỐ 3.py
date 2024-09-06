from math import *

def check (s):
    for i in range(0, len(s)):
        if (s[i] != '0') and (s[i] != '1') and (s[i] != '2'):
            return False
    return True

test = int(input())
while test > 0:
    test -= 1
    n = input()
    if(check(n)) : print("YES")
    else : print("NO")
