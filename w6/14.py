s = input()

def pangram(s):
    s.lower()
    a = set()
    for i in range(len(s)):
        if s[i] in 'qwertyuiopasdfghjklzxcvbnm':
            a.add(s[i])
    
    if len(a) == 26:
        print('Pangram')
    else:
        print('Not pangram')

pangram(s)