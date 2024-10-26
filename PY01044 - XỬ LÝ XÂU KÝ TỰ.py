words1 = set(input().lower().split())
words2 = set(input().lower().split())

union = sorted(words1 | words2)
intersection = sorted(words1 & words2)

print(" ".join(union))
print(" ".join(intersection))
'''
Lap trinh huong doi tuong
Ngon ngu lap trinh C++
'''