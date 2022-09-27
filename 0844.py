a, b = map(int, input().split())
s = int((a * b) ** 0.5)
if s * s == a * b:
  print(s)
else:
  print(0)