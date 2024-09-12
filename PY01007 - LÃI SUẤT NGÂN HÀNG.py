from math import *

test = int(input())
while test > 0:
    test -= 1
    n, x, m = map(float, input().split())

    m /= n
    x /= 100
    years = 0
    while True:
        if ((1 + x) ** years) >= m:
            break
        years += 1
    
    print(years)
