k = int(input())
n = int(input())

cnt1 = 1
cnt1 += n // k

cnt2 = (n - (n // k) * k)

print(cnt1, cnt2)