import re

n = int(input())

pattern = '<[a-z](\w|-|\.)+\@?[a-z]+\.[a-z]{1, 3}>'

for i in range(n):
    x, y = input().split()
    match = re.match(pattern, y)
    if match:
        print(x, y)
