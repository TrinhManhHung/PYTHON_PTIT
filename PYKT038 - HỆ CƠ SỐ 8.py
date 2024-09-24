from math import *

def PhanTich(s):
    if s == '000': return '0'
    if s == '001': return "1"
    if s == '010': return "2"
    if s == '011': return "3"
    if s == '100': return "4"
    if s == '101': return "5"
    if s == '110': return "6"
    if s == '111': return "7"
    return ""

s = input()
s = s.lstrip('0')

n = 3 - (len(s) % 3)
if n != 3:
    s = '0' * n + s

for i in range(0, len(s) - 2, 3):
    print(PhanTich(s[i:i+3]), end = "")