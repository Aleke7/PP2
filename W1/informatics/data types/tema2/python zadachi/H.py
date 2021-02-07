s = input()

print(s[:s.index('h')] + s[s.rindex('h'):s.index('h'):-1] + s[s.rindex('h'):])