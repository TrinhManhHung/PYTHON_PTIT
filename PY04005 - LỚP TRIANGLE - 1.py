from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, b):
        return sqrt((b.x - self.x) ** 2 + (b.y - self.y) ** 2)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def chuVi(self):
        a = self.p1.distance(self.p2)
        b = self.p1.distance(self.p3)
        c = self.p2.distance(self.p3)
        if(2*max(a, b, c) >= a+b+c): print("INVALID")
        else:
            print("{:.3f}".format(a+b+c))

if __name__ == '__main__':
    a = []
    t = int(input())
    for T in range(t):
        a += [float(i) for i in input().split()]
    i = 0
    for idx in range(t):
        x = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
        x.chuVi()
        i += 6
'''
3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0
'''