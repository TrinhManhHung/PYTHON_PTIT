from math import *

a, k, n = map(int, input().split())

tam = 1
check = False
while k * tam <= n:
    if k * tam - a > 0:
        print(k * tam - a, end = " ")
        check = True
    tam += 1

if(check == False):
    print(-1)