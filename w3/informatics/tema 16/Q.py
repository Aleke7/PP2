from collections import Counter

n = int(input())

tree = {}
for i in range(n - 1):
    child, parent = input().split()
    tree[child] = parent

if parent in tree.keys():
    cnt = Counter(sorted(tree))

for i in sorted(cnt.keys(), key = cnt.get):
    print(i)