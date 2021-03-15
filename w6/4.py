s = input()

def reversing(s):
    rs = ''
    for i in range(len(s)):
        rs += s[len(s) - 1 - i]
    return rs
    
print(reversing(s))

# print(s[::-1])