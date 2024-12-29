from math import *
from functools import cmp_to_key

class ThiSinh:
    def __init__(self, id, name, diem, dtoc, kvuc):
        self.id = "TS" + f'{id:02d}'
        self.name = name
        self.diem = diem
        self.dtoc = dtoc
        self.kvuc = kvuc

    def chuanHoaTen(self):
        arr = self.name.strip().lower().split()
        ten = ''
        for x in arr:
            ten += x[0].upper() + x[1:] + ' '
        self.name = ten.strip()

    def getUuTien(self):
        sum = 0
        if self.kvuc == '1': sum += 1.5
        if self.kvuc == '2': sum += 1
        if self.dtoc != 'Kinh': sum += 1.5
        return sum
    def getDiem(self):
        return self.diem + self.getUuTien()
    def getStatus(self):
        if self.getDiem() >= 20.5: return "Do"
        return "Truot"

    def __str__(self):
        self.chuanHoaTen()
        return f'{self.id} {self.name} {self.getDiem():.01f} {self.getStatus()}'

def cmp(a, b):
    if a.getDiem() != b.getDiem():
        if a.getDiem() < b.getDiem(): return 1
        return -1
    if a.id < b.id: return -1
    return 1
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        thiSinh = ThiSinh(i+1, input(), float(input().strip()), input().strip(), input().strip())
        arr.append(thiSinh)

    arr.sort(key = cmp_to_key(cmp))
    for x in arr:
        print(x)
'''
2
Nguyen  hong ngat
22
Kinh
1
  Chu thi MINh
14
Dao
3
'''