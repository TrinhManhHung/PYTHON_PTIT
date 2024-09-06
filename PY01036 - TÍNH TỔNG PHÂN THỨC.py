from math import *
#input
test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    sum = 0
    #case 1
    if n % 2 == 1:
        for i in range(1, n+1, 2):
            sum += 1/i
    #case 2
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            sum += 1/i
    #output
    formatted_x = "{:.6f}".format(sum)
    print(formatted_x)
