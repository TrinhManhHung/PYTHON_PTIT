from math import *

def check(a, b):
    n = len(a)
    for i in range(0, n):
        if a[i] > b[i]:
            return False
    return True


for t in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])

    if check(a, b):
        print("YES")
    else :
        print("NO")
'''
2
4
7 5 3 2
5 4 8 7
8
7 5 3 2 5 105 45 10
2 4 0 5 6 9 75 84 
'''
