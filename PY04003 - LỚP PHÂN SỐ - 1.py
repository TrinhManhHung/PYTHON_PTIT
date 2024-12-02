from decimal import *
from math import *

def gcd(a, b):
    if(b == 0): return a
    return gcd(b, a % b)

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def process(self):
        uoc = gcd(self.tu, self.mau)
        self.tu /= uoc
        self.mau /= uoc
        return self

if __name__ == '__main__':
    a, b = map(int, input().split())
    x = PhanSo(a, b)
    x.process()
    print(int(x.tu), '/', int(x.mau), sep = '') 








'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other_point):
        distancee = sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        formatted_num =  f"{distancee:.4f}"
        return formatted_num
    
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
'''
'''
123 456
'''