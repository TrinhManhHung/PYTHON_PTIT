from math import *

fibo_list = [1, 1]
for i in range(2, 93):
    fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

test = int(input())
while test > 0:
    test -= 1
    start, end = map(int, input().split())
    for i in range(start - 1, end):
        print(fibo_list[i], end = ' ')
    print()
    


'''

'''
