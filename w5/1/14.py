with open('14_1.txt', 'r') as f:
    txt1 = f.read().split('\n')

with open('14_2.txt', 'r') as ff:
    txt2 = ff.read().split('\n')

for i, j in zip(txt1, txt2):
    print(i, j)