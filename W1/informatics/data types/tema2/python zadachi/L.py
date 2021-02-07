s = input()

s1 = s[:s.index('h') + 1]
s2 = s[s.index('h') + 1:s.rindex('h')]
s3 = s[s.rindex('h'):]

print(s1 + s2.replace('h', 'H') + s3)