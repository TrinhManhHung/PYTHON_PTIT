from math import *
from functools import cmp_to_key
class SinhVien:
    def __init__(self, name, ac, sub):
        self.name = name
        self.ac = ac
        self.sub = sub
    def __str__(self):
        return f'{self.name} {self.ac} {self.sub}'

def cmp(a, b):
    if a.ac != b.ac:
        return b.ac - a.ac
    if a.sub != b.sub:
        return a.sub - b.sub
    if a.name < b.name: return -1
    return 1

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        name = input()
        ac, sub = map(int, input().split())
        sv = SinhVien(name, ac, sub)
        arr.append(sv)

    arr.sort(key = cmp_to_key(cmp))
    for x in arr:
        print(x)
'''
2
Nguyen Van Nam
168 600
Tran Thi Ngoc
168 600
'''