f = open('16.txt', 'r')

if f.closed:
    print('Closed')
else:
    print('Not closed')

f.close()

if f.closed:
    print('Closed')
else:
    print('Not closed')