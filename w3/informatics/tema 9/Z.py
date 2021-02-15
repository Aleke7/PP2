a = list(map(int,input().split()))
n = int(input())

k = n % len(a)

if k > 0:
    a = a[-k:] + a[:-k]
else:
    k = abs(k)
    a = a[k:] + a[:k]

print(*a)


