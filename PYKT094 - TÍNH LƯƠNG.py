from math import *
from functools import cmp_to_key

phongBan = dict()

class NhanVien:
    def __init__(self, id, name, sal1day, day):
        self.id = id
        self.name = name
        self.sal1mon = sal1day * day
        self.depart = phongBan[self.id[3:]]

    def getHeSo(self):
        group = self.id[0]
        years = int(self.id[1:3])
        if years >= 1 and years <= 3:
            if group == 'A': return 10
            if group == 'B': return 10
            if group == 'C': return 9
            if group == 'D': return 8
        if years >= 4 and years <= 8:
            if group == 'A': return 12
            if group == 'B': return 11
            if group == 'C': return 10
            if group == 'D': return 9
        if years >= 9 and years <= 15:
            if group == 'A': return 14
            if group == 'B': return 13
            if group == 'C': return 12
            if group == 'D': return 11
        if years >= 16:
            if group == 'A': return 20
            if group == 'B': return 16
            if group == 'C': return 14
            if group == 'D': return 13
        return 0

    def getLuong(self):
        return self.sal1mon * self.getHeSo() * 1000

    def __str__(self):
        return f'{self.id} {self.name} {self.depart} {self.getLuong()}'

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        tmp = list(input().split())
        id = tmp[0]
        phong = ''
        for i in range(1, len(tmp)):
            phong += tmp[i] + " "
        phongBan[id] = phong.strip()

    arr = []
    n = int(input())
    for _ in range(n):
        nv = NhanVien(input(), input(), int(input()), int(input()))
        arr.append(nv)

    for x in arr:
        print(x)
'''
2
HC Hanh chinh
KH Ke hoach Dau tu
2
C06HC
Tran Binh Minh
65
25
D03KH
Le Hoa Binh
59
24
'''