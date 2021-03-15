a = input().split()

def unique(iterable):
    return sorted(list(set(iterable)))

print(unique(a))