s = input()

cnt = 0
for i in range(len(s)):
    if s[i] == 'f':
        cnt += 1
    if cnt == 2:
        print(i)
        break

if cnt == 1:
    print(-1)
if cnt == 0:
    print(-2)