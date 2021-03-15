n = int(input())

def perfect(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    if sum(divisors[:len(divisors) - 1]) == n and sum(divisors) // 2 == n:
        print('Perfect number')
    else:
        print('Not perfect number')

perfect(n)