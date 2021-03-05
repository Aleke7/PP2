import re
n = int(input())

l = list()
for i in range(n):
    s = input()
    l.append(s)


pattern = '^(7|8|9)[0-9]{9}$'

for i in l:
    match = re.match(pattern, i)
    if match:
        print('YES')
    else:
        print('NO')
