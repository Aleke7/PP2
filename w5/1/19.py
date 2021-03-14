with open('19_1.txt', 'r') as f:
    txt1 = f.read()

with open('19_2.txt', 'r') as f:
    txt2 = f.read()

l = []
l.append(txt2)
l.append(txt1)

print(l)