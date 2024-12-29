from math import *
from functools import cmp_to_key

mp  = {}
class Phim:
    def __init__(self, id, idtype, date, name, size):
        self.id = "P" + f'{id:03d}'
        self.type = mp[idtype]
        self.date = date
        self.name = name
        self.size = size

    def getDate(self):
        return self.date
    def getSize(self):
        return self.size
    def getName(self):
        return self.name
    def __str__(self):
        return f'{self.id} {self.type} {self.date} {self.name} {self.size}'

def cmp(a, b):
    datea = a.getDate()
    ya = int(datea[6:])
    ma = int(datea[3:5])
    da = int(datea[0:2])
    dateb = b.getDate()
    yb = int(dateb[6:])
    mb = int(dateb[3:5])
    db = int(dateb[0:2])
    if ya != yb: return ya - yb
    if ma != mb: return ma - mb
    if da != db: return da - db
    if a.getName() != b.getName():
        if(a.getName() < b.getName()): return -1
        else: return 1
    return b.getSize() - a.getSize()

if __name__ == '__main__':
    m, n = map(int, input().split())
    for i in range(m):
        id = "TL" + f'{(i+1):03d}'
        s = input()
        mp[id] = s
    arr = []
    for i in range(n):
        phim = Phim(i+1, input(), input(), input(), int(input()))
        arr.append(phim)

    arr.sort(key = cmp_to_key(cmp))
    for x in arr:
        print(x)


'''
2 3
Hai huoc
Tinh cam
TL001
25/11/2021
Phim so 1
10
TL001
04/12/2021
Phim so 2
15
TL002
25/11/2021
Phim so 3
5
'''