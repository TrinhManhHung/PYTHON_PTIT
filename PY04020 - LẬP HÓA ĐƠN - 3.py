from math import *
from functools import cmp_to_key

class KhachHang:
    def __init__(self, id, name, cnt, price, discount):
        self.id = id
        self.name = name
        self.cnt = cnt
        self.price = price
        self.discount = discount

    def getTongTien(self):
        return self.price * self.cnt - self.discount
    def __str__(self):
        return f'{self.id} {self.name} {self.cnt} {self.price} {self.discount} {self.getTongTien()}'

def cmp(a, b):
    return b.getTongTien() - a.getTongTien()

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        kh = KhachHang(input(), input(), int(input()), int(input()), int(input()))
        arr.append(kh)

    arr.sort(key = cmp_to_key(cmp))
    for x in arr:
        print(x)

'''
3
ML01
May lanh SANYO
12
4000000
2400000
ML02
May lanh HITACHI
4
2550000000
0
ML03
May lanh NATIONAL
5
3000000
150000
'''