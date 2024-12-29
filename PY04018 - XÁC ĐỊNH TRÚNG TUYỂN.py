from math import *
from functools import cmp_to_key

class GiaoVien:
    def __init__(self, id, name, idMH, diem1, diem2):
        self.id = "GV" + f'{id:02d}'
        self.name = name
        self.idMH = idMH
        self.diem1 = diem1
        self.diem2 = diem2

    def getMonHoc(self):
        if self.idMH[0] == 'A': return 'TOAN'
        if self.idMH[0] == 'B': return 'LY'
        if self.idMH[0] == 'C': return 'HOA'

    def getUuTien(self):
        if self.idMH[1] == '1': return 2
        if self.idMH[1] == '2': return 1.5
        if self.idMH[1] == '3': return 1
        return 0
    def getDiem(self):
        return self.diem1 * 2 + self.diem2 + self.getUuTien()
    def getTrangThai(self):
        if(self.getDiem() >= 18): return "TRUNG TUYEN"
        else: return "LOAI"

    def __str__(self):
        return f'{self.id} {self.name} {self.getMonHoc()} {self.getDiem():.01f} {self.getTrangThai()}'

def cmp(a, b):
    return b.getDiem() - a.getDiem()

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        gv = GiaoVien(i + 1, input(), input(), float(input()), float(input()))
        arr.append(gv)

    arr.sort(key = cmp_to_key(cmp))
    for x in arr:
        print(x)

'''
3
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
'''