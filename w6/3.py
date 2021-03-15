a = [int(i) for i in input().split()]

def prod(iterable):
    mltp = 1
    for i in a:
        mltp *= i
    return mltp

print(prod(a))
