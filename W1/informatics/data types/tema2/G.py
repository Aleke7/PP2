s = input()

print(s[:s.index('h')] + s[s.rindex('h') + 1:])
#print(s[:s.find('h')] + s[s.rfind('h') + 1:])