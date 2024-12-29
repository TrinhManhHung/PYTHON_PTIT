from math import *
from functools import cmp_to_key
class KhachHang:
    def __init__(self, id, name, start, end):
        self.id = "KH" + f'{id:02d}'
        self.name = name
        self.start = start
        self.end = end
    def getHoaDon(self):
        sum = self.end - self.start
        res = 0
        if sum > 0:
            units = min(50, sum)
            res += units * 100
            sum -= 50
        if sum > 0:
            units = min(50, sum)
            res += units * 150
            sum -= 50
        if sum > 0:
            res += sum * 200

        if self.end - self.start <= 50: res = res * 102 / 100
        elif self.end - self.start <= 100: res = res * 103 / 100
        else: res = res * 105 / 100
        return res
    def __str__(self):
        return f'{self.id} {self.name} {round(self.getHoaDon())}'
def cmp(a, b):
    if a.getHoaDon() > b.getHoaDon(): return -1
    return 1
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        khachHang = KhachHang(i + 1, input(), int(input()), int(input()))
        arr.append(khachHang)

    arr.sort(key = cmp_to_key(cmp))
    for i in range(n):
        print(arr[i])

'''
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
'''