from math import *
from functools import cmp_to_key
class SinhVien:
    def __init__(self, id, name, diem1, diem2):
        self.id = "TS0" + str(id)
        self.name = name
        self.diem1 = diem1
        if diem1 > 10: self.diem1 = diem1 / 10
        self.diem2 = diem2
        if diem2 > 10: self.diem2 = diem2 / 10
    def getDiem(self):
        return (self.diem1 + self.diem2) / 2
    def getStatus(self):
        if(self.getDiem() < 5): return "TRUOT"
        elif (self.getDiem() < 8): return "CAN NHAC"
        elif (self.getDiem() <= 9.5): return "DAT"
        else: return "XUAT SAC"
    def __str__(self):
        return f'{self.id} {self.name} {self.getDiem():.02f} {self.getStatus()}'

def cmp(a, b):
    if a.getDiem() > b.getDiem(): return -1
    return 1
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        x = SinhVien(i+1, input(), float(input()), float(input()))
        arr.append(x)

    arr.sort(key = cmp_to_key(cmp))

    for x in arr:
        print(x)
'''
3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
'''