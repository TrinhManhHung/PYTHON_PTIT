from math import *

def checkXenKe(n) :
    if len(n) % 2 == 0: return False
    if n[0] == n[1]: return False
    for i in range(0, len(n), 2):
        if n[i] != n[0]: return False
    
    return True

test = int(input())
for i in range(test):
    n = input()
    if(checkXenKe(n)): print("YES")
    else: print("NO")


'''
2
2324272921262
13141516
'''