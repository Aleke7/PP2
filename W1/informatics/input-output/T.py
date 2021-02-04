n = int(input())

d1 = n // 1000
d2 = (n // 100) % 10
d3 = (n // 10) % 10
d4 = n % 10

s1 = d1 * 10 + d2
s2 = d4 * 10 + d3

print(s1 - s2 + 1)