a = int(input())
if a > 0:
    b = (1 + a) * a // 2
else:
    b = (-1 + a) * abs(a) // 2 + 1
print(b)