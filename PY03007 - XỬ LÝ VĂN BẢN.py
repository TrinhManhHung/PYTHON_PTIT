import sys
words = list(sys.stdin.read().lower().split())

words[0] = words[0][0].upper() + words[0][1:]
for i in range(0, len(words)):
    if words[i][len(words[i])-1] == '.' or words[i][len(words[i])-1] == '?' or words[i][len(words[i])-1] == '!':
        words[i] = words[i][:len(words[i]) - 1]
        print(words[i])
        if i+1 < len(words): words[i+1] = words[i+1][0].upper() + words[i+1][1:]
    else:
        print(words[i], end = " ")

'''
ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
    vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.
'''

