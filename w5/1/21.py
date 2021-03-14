with open('21.txt', 'w') as f:
    for i in range(65, 91):
        f.write(str(i - 64) + ')' + chr(i))
        f.write('\n')
with open('21.txt', 'r') as f:
    print(f.read())