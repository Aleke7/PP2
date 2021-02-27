n, m = input().split()

an, am = set(), set()

for i in range(int(n)):
    an.add(int(input()))

for i in range(int(m)):
    am.add(int(input()))

print(len(an.intersection(am)))

for i in sorted(an.intersection(am)):
    print(i, end = ' ')
print()

print(len(an.difference(am)))

for i in sorted(an.difference(am)):
    print(i, end = ' ')
print()

print(len(am.difference(an)))

for i in sorted(am.difference(an)):
    print(i, end = ' ')
