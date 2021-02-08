from typing import Sized


n = int(input())

mltp = 1
summ = 0

while n != 0:
    summ += n % 10
    mltp *= n % 10
    n //= 10

print(mltp - summ)