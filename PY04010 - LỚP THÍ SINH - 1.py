from math import *

class ThiSinh:
    def __init__(self, name, birth, mon1, mon2, mon3):
        self.name = name
        self.birth = birth
        self.mon1 = mon1
        self.mon2 = mon2
        self.mon3 = mon3
    def inRa(self):
        tongDiem = self.mon1 + self.mon2 + self.mon3
        print(self.name, self.birth, "{:.1f}".format(tongDiem))

if __name__ == "__main__":
    thiSinh = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
    thiSinh.inRa()

'''
Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5
'''