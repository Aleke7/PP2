a = input().split()

mx = 0
k = None
for i in a:
    if mx < len(i):
        mx = len(i)
        k = i

print(k)
print(mx)
    