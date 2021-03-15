n = int(input())

def factor(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(f"Input a number to compute the factiorial : {n}")
print(factor(n))

# import math
# n = int(input())
# print(math.factorial(n))