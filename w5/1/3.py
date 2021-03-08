with open('3.txt', 'a') as f:
  txt = f.write(input())
  
with open('3.txt', 'r') as f:
  txt = f.read()
  
print(txt)