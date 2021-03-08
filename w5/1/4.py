with open('4.txt', 'r') as f:
    txt = f.readlines()

n = int(input())

for i in txt[-n:]:
    print(i)