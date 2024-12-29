from math import *
from functools import cmp_to_key

class SinhVien:
    def __init__(self, id, name, arr):
        self.id = "HS" + f'{id:02d}'
        self.name = name
        self.total = (sum(arr) + arr[0] + arr[1])

    def getDiem(self):
        res = round(self.total / 12 + 0.01, 1)
        return res
    def getStatus(self):
        tmp = round(self.getDiem(), 1)
        if self.getDiem() >= 9: return "XUAT SAC"
        if self.getDiem() >= 8: return "GIOI"
        if self.getDiem() >= 7: return "KHA"
        if self.getDiem() >= 5: return "TB"
        return "YEU"

    def __str__(self):
        return f'{self.id} {self.name} {self.getDiem():.01f} {self.getStatus()}'

def cmp(a, b):
    if a.getDiem() != b.getDiem():
        if a.getDiem() < b.getDiem(): return 1
        return -1
    if a.id < b.id: return -1
    return 1

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        arr = list(map(float, input().split()))
        sinhVien = SinhVien(i+1, name, arr)
        a.append(sinhVien)

    a.sort(key = cmp_to_key(cmp))
    for x in a:
        print(x)

'''
3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
'''