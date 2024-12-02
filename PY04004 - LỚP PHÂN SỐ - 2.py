from decimal import *
from math import *

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)
def lcm(a, b):
    return a * b / gcd(a, b)

class PhanSo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum(self, other):
        mauChung = lcm(self.y, other.y)
        tuChung = self.x * (mauChung / self.y) + other.x * (mauChung / other.y)
        uocChung = gcd(tuChung, mauChung)
        tuChung /= uocChung
        mauChung /= uocChung
        return '{}/{}'.format(int(tuChung), int(mauChung))
        
if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    x1 = PhanSo(a, b)
    x2 = PhanSo(c, d)
    print(x1.sum(x2))





'''
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