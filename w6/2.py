a = [int(i) for i in input().split()]

# print(sum(a))

def sm(iterable):
    summ = 0
    for i in iterable:
        summ += i
    return summ

print(sm(a))