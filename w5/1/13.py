with open('13_copy.txt', 'r') as f:
    with open('13_paste.txt', 'w') as ff:
        ff.write(f.read())

# import shutil
# shutil.copy('13_copy.txt', '13_paste.txt')