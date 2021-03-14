l = input().split()

with open('12.txt', 'w') as f:
    for i in l:
        f.write(f'{i}\n')