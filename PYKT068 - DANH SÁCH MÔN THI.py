from math import *
from functools import cmp_to_key
from itertools import combinations

class MonHoc:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

    def __str__(self):
        return f'{self.id} {self.name} {self.type}'

def cmp(a, b):
    if a.id < b.id: return -1
    return 1

if __name__ == '__main__':
    n = int(input())
    arr = []
    for x in range(n):
        mh = MonHoc(input(), input(), input())
        arr.append(mh)
    arr.sort(key = cmp_to_key(cmp))
    for x in arr:
        print(x)

