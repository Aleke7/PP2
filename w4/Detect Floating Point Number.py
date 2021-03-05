import re

n = int(input())

l = []
for i in range(n):
    s = input()
    l.append(s)

pattern = '^(\+?|\-?|\.?|\d+|\+?\.?|\-?\.?)(\d+)\.?(\d+)$'

for i in l:
    match = re.match(pattern, i)
    if match:
        print("True")
    else:
        print("False")