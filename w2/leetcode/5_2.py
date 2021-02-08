n = input()

mltp = 1
summ = 0

for i in range(len(n)):
    summ += int(n[i])
    mltp *= int(n[i])

print(mltp - summ)