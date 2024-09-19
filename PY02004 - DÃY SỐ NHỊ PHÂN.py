from math import *

n = int(input())
list = list(map(int, input().split()))
cnt = 0
for i in range(1, n):
    if(list[i] != list[i-1]):
        cnt += 1

print(cnt)


'''
1
1221
1234567891011121314151617181920212223242526272829
'''
