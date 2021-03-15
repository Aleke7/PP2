a, b, c = [int(i) for i in input().split()]

# print(max(a, b, c))

def mx(a, b, c):
    if a < b < c or b < a < c:
        return c
    if a < c < b or c < a < b:
        return b
    if c < b < a or b < c < a:
        return a

print(mx(a, b, c))
