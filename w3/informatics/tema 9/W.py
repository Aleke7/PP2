a = list(map(int,input().split()))
b = []
c = []
for i in a:
    if i != 0:
        b.append(i)
    else:
        c.append(i)

for i in b + c:
    print(i, end = ' ')
