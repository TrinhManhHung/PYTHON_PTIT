from math import *

test = int(input())

while test > 0:
    test -= 1
    x1, x2 = map(int, input().split())
    mi = min(x1, x2)
    ma = max(x1, x2)
    x1 = str(mi)
    x2 = str(ma)

    ip = input().split()
    if len(ip) == 1:
        n = ip[0]
        m = input()
    else:
        n, m = ip

    maxSum = int(n.replace(x1, x2)) + int(m.replace(x1, x2))
    minSum = int(n.replace(x2, x1)) + int(m.replace(x2, x1))

    print(minSum, maxSum)

    