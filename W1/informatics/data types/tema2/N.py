s = input()

p = ''
for i in range(len(s)):
    if i % 3 != 0:
        p += s[i]
    
print(p)
    