s = input().split()
s = ''.join(s)

def palindrome(s):
    rs = ''
    for i in range(len(s)):
        rs += s[len(s) - 1 - i]
    
    if s == rs:
        print('Palindrome')
    else:
        print('Not palindrome')

palindrome(s)