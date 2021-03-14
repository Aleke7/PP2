with open('17.txt', 'r') as f:
    txt = f.read().strip('\n').split()

print(*txt)