from math import *
from functools import cmp_to_key

class KhachHang:
    def __init__(self, id, name, type, begin, end):
        self.id = "KH" + f'{id:02d}'
        self.name = name
        self.type = type
        self.use = end - begin
        self.tienTrong = 0
        self.tienNgoai = 0
        self.tienVAT = 0
        self.calculator()

    def chuanHoa(self):
        tmp = self.name.lower().strip().split()
        ten = ''
        for x in tmp:
            ten += x[0].upper() + x[1:] + ' '
        self.name = ten.strip()

    def calculator(self):
        if self.type == 'A':
            self.tienTrong = min(self.use, 100) * 450
            self.use = max(0, self.use - 100)
        if self.type == 'B':
            self.tienTrong = min(self.use, 500) * 450
            self.use = max(0, self.use - 500)
        if self.type == 'C':
            self.tienTrong = min(self.use, 200) * 450
            self.use = max(0, self.use - 200)

        self.tienNgoai = self.use * 1000
        self.tienVAT = int(self.tienNgoai / 20)

    def __str__(self):
        self.chuanHoa()
        return f'{self.id} {self.name} {self.tienTrong} {self.tienNgoai} {self.tienVAT} {self.tienVAT + self.tienNgoai + self.tienTrong}'

def cmp(a, b):
    tmp = (b.tienVAT + b.tienNgoai + b.tienTrong) - (a.tienVAT + a.tienNgoai + a.tienTrong)
    if tmp > 0: return 1
    return -1

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        name = input()
        tmp = list(input().split())
        kh = KhachHang(i+1, name, tmp[0].strip(), int(tmp[1]), int(tmp[2]))
        arr.append(kh)

    arr.sort(key = cmp_to_key(cmp))
    for x in arr:
        print(x)
'''
2
 nGuyEn Hong Ngat
C 200 278
 Chu thi    minh
A 120 160
'''