from math import *

t = int(input())
for T in range(t):
    s = input()
    arr = []
    for x in s:
        if x == '(' or x == ')':
            arr.append(x)
    
    res = arr
    cnt = 0
    stack = []
    for i in range(0, len(arr)):
        if arr[i] == '(':
            cnt += 1
            res[i] = cnt
            stack.append(i)
        elif arr[i] == ')':
            res[i] = res[stack[len(stack)-1]]
            stack.pop()
    
    for x in res:
        print(x, end = ' ')
    print()
'''
2
(a + (b *c) ) + (d/e)
( ( () ) ( () ) )
'''
