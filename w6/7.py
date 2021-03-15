s = input()

def count_string(s):
    cnt_l = 0
    cnt_u = 0
    for i in range(len(s)):
        if s[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            cnt_u += 1
        if s[i] in 'qwertyuiopasdfghjklzxcvbnm':
            cnt_l += 1
    print(f'No. of Upper case characters : {cnt_u}')
    print(f'No. of Lower case Characters : {cnt_l}')

count_string(s)