s = input()

p = ''
for i in range(len(s)):
    if s[i] == 'G':
        p += 'G'
    elif s[i] == '(' and s[i + 1] == ')':
        p += 'o'
    elif s[i] == '(' and s[i+1] == 'a' and s[i+2] == 'l' and s[i+3] == ')':
        p += 'al'

print(p)