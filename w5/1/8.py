with open('8.txt', 'r') as f:
    txt = f.read().split()
mxlen = 0
mxword = ''
for i in txt:
    if mxlen < len(i):
        mxlen = len(i)
        mxword = i

print(mxword)