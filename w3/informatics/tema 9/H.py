a = list(map(int,input().split()))

mn = 9999

for i in a:
    if i < mn and i > 0:
        mn = i

print(mn)