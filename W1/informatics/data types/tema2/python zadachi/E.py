s = input()

cnt = len(s) - len(s.replace('f', ''))

if cnt == 0:
    print()
elif cnt == 1:
    print(s.index('f'))
elif cnt >= 2:
    print(s.index('f'), s.rindex('f'))
