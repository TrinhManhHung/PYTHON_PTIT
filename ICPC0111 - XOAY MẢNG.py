from math import *

test = int(input())

while test > 0:
    test -= 1
    n, d = map(int, input().split())
    my_list = list(map(int, input().split()))

    for i in range(d, n):
        print(my_list[i], end = " ")
    for i in range(0, d):
        print(my_list[i], end = " ")
    print()

    