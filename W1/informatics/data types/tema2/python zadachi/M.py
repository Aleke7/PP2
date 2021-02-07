s = input()

p = ''
for i in range(len(s) - 1):
    p += s[i] + '*'
    

print(p + s[len(s) - 1])