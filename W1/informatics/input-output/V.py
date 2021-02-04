a, b = int(input()), int(input())

s1 = (a // b * a) + (b // a * b);
s2 = a // b + b // a;

print(s1 // s2)