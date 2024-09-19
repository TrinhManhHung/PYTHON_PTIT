from math import *

def solve(s):
    s1 = s[::-1]
    for i in range(1, len(s)):
        if abs((ord(s[i]) - ord(s[i-1]))) != abs(ord(s1[i]) - ord(s1[i-1])):
            return False
    return True

test = int(input())
while test > 0:
    test -= 1
    s = input()
    if solve(s):
        print("YES")
    else :
        print("NO")


'''
2
acxz
bcxz
'''
