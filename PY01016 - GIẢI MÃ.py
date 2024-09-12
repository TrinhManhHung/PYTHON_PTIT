from math import *

test = int(input())
while(test > 0):
    test -= 1
    s = input()
    for i in range(len(s)):
        if s[i].isdigit():
            for j in range(int(s[i])):
                print(s[i-1], end = '')

    print()




