a, b = int(input()), int(input())

def make_adder(x):
       def adder(y):
           return x + y
       return adder

f = make_adder(a)
print(f(b))