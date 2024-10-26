from math import *

test = int(input())
while test > 0:
    test -= 1
    n, k = map(int, input().split())

    while True:
        loga = int(log2(k))
        if k == 2 ** loga:
            print(chr(ord('A') + loga))
            break
        k -= 2 ** loga