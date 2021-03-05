import re

s = input()

pattern = '[^0-9]'

result = re.split(pattern, s)

for i in result:
    print(i)