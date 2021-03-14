import os

os.chdir('20')
for i in range(65, 91):
    with open(chr(i) + '.txt', 'w') as f:
        f.write('')