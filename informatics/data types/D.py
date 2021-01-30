d = int(input())

h = (d * 12) // 360
m = (((d * 12) - (h * 360)) * 60) // 360

print(f"It is {h} hours {m} minutes.")