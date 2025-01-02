from math import *
from functools import cmp_to_key

class SinhVien:
    def __init__(self, id, name, mon1, mon2, mon3):
        self.id = "SV" + f'{id:02d}'
        self.name = name
        self.total = mon1 * 3 + mon2 * 3 + mon3 * 2

    def chuanHoa(self):
        a = self.name.strip().lower().split()
        ten = ''
        for x in a:
            ten += x[0].upper() + x[1:] + " "
        self.name = ten.strip()

    def getDiem(self):
        return '{:.2f}'.format(self.total / 8 + 0.001)

    def __str__(self):
        self.chuanHoa()
        return f'{self.id} {self.name} {self.getDiem()}'

def cmp(a, b):
    if a.getDiem() != b.getDiem():
        if a.getDiem() > b.getDiem(): return -1
        return 1
    else:
        if a.id < b.id: return -1
        return 1

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        sv = SinhVien(i+1, input(), float(input()), float(input()), float(input()))
        arr.append(sv)

    arr.sort(key = cmp_to_key(cmp))
    stt = 1
    for i in range(len(arr)):
        if i == 0 or arr[i].getDiem() == arr[i-1].getDiem():
            print(arr[i], stt)
        else:
            print(arr[i], i+1)
            stt = i+1

'''
4
 ha Thi kieu     anh
7
6
7
Pham    THI  HAO
6
7
6
 ha Thi kieu     anh1
7
6
7
Pham    THI  HAO1
6
7
6.5
'''