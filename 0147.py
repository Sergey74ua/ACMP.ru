N = int(input())
a = 0
b = 1
for i in range(N):
  a, b = b, a + b
print(a)