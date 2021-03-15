import math

n = int(input())

def isPrime(n):
    flag = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            flag = False
    
    if flag:
        print(f'{n} is prime number')
    else:
        print(f'{n} is not prime number')

isPrime(n)