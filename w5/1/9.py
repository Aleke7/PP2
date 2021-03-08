with open('9.txt', 'r') as f:
    txt = f.read()

cnt = 1
for i in txt:
    if i == '\n':
        cnt += 1

print(f"Number of lines in the file: {cnt}")