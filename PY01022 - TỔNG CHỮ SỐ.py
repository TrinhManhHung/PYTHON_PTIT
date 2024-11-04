from math import *

n = int(input())

ans = 0
s = str(n)
if len(s) == 1: print(1)
else:
    while len(s) > 1:
        sum = 0
        for x in s:
            sum += ord(x) - 48
        s = str(sum)
        ans += 1

    print(ans)
'''
4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7
'''