from collections import Counter

with open('10.txt', 'r') as f:
    txt = f.read().split()

cnt = Counter(txt)

print(f"Number of words in the file : {cnt}")