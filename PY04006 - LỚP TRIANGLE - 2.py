from decimal import *
from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other_point):
        distancee = sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distancee

class Triangle:
    def __init__ (self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def dienTich(self):
        x = self.a.distance(self.b)
        y = self.a.distance(self.c)
        z = self.b.distance(self.c)
        if(max(x, y, z) * 2 >= x + y + z) : print('INVALID')
        else:
            res = sqrt((x+y+z) * (-z +x+y) * (-x+y+z) *(-y+z+x)) / 4
            print("{:.2f}".format(res))

if __name__ == '__main__':
    a = []
    t = int(input())
    for x in range(t):
        a += [float(i) for i in input().split()]
    i = 0
    for index in range(t):
        triagle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
        triagle.dienTich()
        i += 6
        

'''
3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0
'''