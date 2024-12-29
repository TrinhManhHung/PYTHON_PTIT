from math import *

class SinhVien:
    def __init__(self, id, name, className):
        self.id = id
        self.name = name
        self.className = className
        self.score = 10
        self.note = ""
    def calculator(self, s):
        cnt_v = s.count('v')
        cnt_m = s.count('m')
        res = cnt_v * 2 + cnt_m
        self.score = max(0, self.score - res)
        if self.score == 0: self.note = ' KDDK'
    def __str__(self):
        return (f'{self.id} {self.name} {self.className} {self.score}{self.note}')

if __name__ == '__main__':
    n = int(input())
    arr = []
    for N in range(n):
        id = input()
        name = input()
        className = input()
        sinhVien = SinhVien(id, name, className)
        arr.append(sinhVien)

    for N in range(n):
        id, s = map(str, input().split())
        for x in arr:
            if x.id == id:
                x.calculator(s)
    for x in arr:
        print(x)

'''
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
'''