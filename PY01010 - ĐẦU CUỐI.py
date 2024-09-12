from math import *

test = int(input())

while test > 0:
    test -= 1
    n = input()
    if n[:2] == n[(len(n)-2):]:
        print("YES")
    else :
        print("NO")
