n = int(input())

a, b = int(input()), int(input())

def check_in_range(n):
    if n in range(a, b + 1):
        print(f'{n} is inside the range {a}-{b}')
    else:
        print(f'{n} is outside the range {a}-{b}')

check_in_range(n)