from math import *
from functools import cmp_to_key

class ThiSinh:
    def __init__(self, name, addr, time):
        self.name = name
        self.addr = addr
        self.time = time
        self.id = ''

        tmp1 = self.addr.lstrip().split()
        tmp2 = self.name.lstrip().split()
        for x in tmp1:
            self.id += x[0]
        for x in tmp2:
            self.id += x[0]

    def getVanToc(self):
        s = 120
        hours = int(self.time[0])
        minutes = int(self.time[2:])
        t = (hours - 6) * 60 + minutes
        t /= 60
        return s / t
    def __str__(self):
        return f'{self.id} {self.name} {self.addr} {round(self.getVanToc())} Km/h'

def cmp (a, b):
    if(a.getVanToc() >= b.getVanToc()): return -1
    return 1
if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        thiSinh = ThiSinh(input(), input(), input())
        arr.append(thiSinh)

    arr.sort(key = cmp_to_key(cmp))
    for x in arr:
        print(x)

'''
3
Tran Vu Minh
Ha Noi
8:30
Vu Ngoc Hoang
Hoa Binh
8:20
Pham Dinh Tan
An Giang
8:45
'''