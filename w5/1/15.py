import random

with open('15.txt', 'r') as f:
    txt = f.read().split('\n')

print(txt[random.randrange(0, len(txt))])
