a = input().split()
#a = [int(i) for i in input().split()]

for i in a[::2]:
    print(i, end = ' ')