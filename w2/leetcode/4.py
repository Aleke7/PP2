gain = list(input().split())

ans = []
ans.append(0)

for i in range(0, len(gain)):
    tmp = int(ans[i]) + int(gain[i])
    ans.append(tmp)

print(max(ans))