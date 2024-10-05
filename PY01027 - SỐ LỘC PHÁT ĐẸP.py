from math import *

s = input()
s = s[::-1]

x1 = '6'
x2 = '86'
x3 = '886'

oke = True
while len(s) >= 1:
    if s[0:1] == x1:
        s = s[1:]
    elif s[0:2] == x2:
        s = s[2:]
    elif s[0:3] == x3:
        s = s[3:]
    else:
        oke = False
        break

if oke:
    print("YES")
else :
    print("NO")
    