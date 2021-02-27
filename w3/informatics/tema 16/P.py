from collections import Counter

f = open('input.txt', 'r')

s = f.read().split()

cnt = Counter(sorted(s))

for i in sorted(cnt.keys(), key = cnt.get, reverse = True):
    print(i)

