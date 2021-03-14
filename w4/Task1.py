import re

with open('input.txt', 'r', encoding='utf-8') as f:
    txt = f.read()

name_of_company = re.search(r'Филиал\sТОО\s\w+\s\w+', txt)
bin_num = re.search(r'\d{12}', txt)
title = re.findall(r'\d+\.\n(.*)', txt)
count = re.findall(r'(\d),\d{3}', txt)
unit_price = re.findall(r'x\s([\d+\s?]+,\d+)', txt)
total_price = re.findall(r'x\s[\d+\s?]+,\d+\n(.*)', txt)
date = re.search(r'\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}', txt)
address = re.search(r'г\.(.*)', txt)

print(f'1. Name of the company: {name_of_company.group()}')
print(f'2. BIN number: {bin_num.group()}')

print('3. For each item:')
for i in range(len(title)):
    print(f'\t {str(i + 1)})' + '——' * 30)
    print(f'\t1. Title —— ({title[i]})')
    print(f'\t2. Cout ——  ({count[i]})')
    print(f'\t3. Unit price —— ({unit_price[i]})')
    print(f'\t4. Total price —— ({total_price[i]})')

print(f'4. Date —— ({date.group()})')
print(f'5. Address —— ({address.group()})')