n = int(input())
a = {}
for i in range(n):
    x, y = [s for s in input().split()]
    a[x] = y
    a[y] = x

c = input()

print(a[c])




