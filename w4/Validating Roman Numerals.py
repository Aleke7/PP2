import re

thousand = "(?:(M){0,3})?"
hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"

pattern = r"^" + thousand + hundred + ten + unit + "$"
s = input()

match = re.match(pattern, s)

if match:
    print(True)
else:
    print(False)