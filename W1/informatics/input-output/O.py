a, b, n = int(input()), int(input()), int(input())

cost = (a * 100 + b) * n
print(cost // 100, cost % 100)