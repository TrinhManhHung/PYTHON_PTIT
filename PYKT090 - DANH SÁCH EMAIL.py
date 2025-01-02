from math import *
from functools import cmp_to_key
from itertools import combinations

if __name__ == '__main__':
    f = open('CONTACT.in', 'r')
    arr = []
    for email in f:
        tmp = email.lower().strip()
        arr.append(tmp)
    res = list(set(arr))
    res.sort()
    for x in res: print(x)

'''
nguyenmanhson@gmail.com
sonnm@ptit.edu.vn
NGUYENMANHSON@gmail.com
SonNM@ptit.edu.vn
NguyenManhSon@GMAIL.com
'''
