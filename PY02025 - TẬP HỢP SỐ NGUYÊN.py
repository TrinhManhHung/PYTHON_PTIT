from math import *

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = sorted(a & b)
d = sorted(a - b)
e = sorted(b - a)

print(*c)
print(*d)
print(*e)

'''
4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7
'''