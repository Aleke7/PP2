n = int(input())
m = int(input())

k = m / n

if k >= 1:
    print(int((m + n - 1) / n))
else:
    print(1)
