from math import *

test = int(input())
while test > 0:
    test -= 1

    s = input()
    sub = input()
    cnt = 0
    start = 0
    end = len(s)
    while s.rfind(sub, start, end) != -1:
        cnt += 1
        end = s.rfind(sub, start, end)
    
    print(cnt)

    


'''
2
1212121112211221121
121
2222222222322292
2222
'''
