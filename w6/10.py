a = [int(i) for i in input().split()]

def take_even_num(iterable):
    even = []
    for i in iterable:
        if i % 2 == 0:
            even.append(i)
    print(even)

take_even_num(a)