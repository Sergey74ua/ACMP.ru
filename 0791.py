n = int(input())
s = ''
if n > 8:
    s += str(n - 8) + ' '
if (n - 1) % 8 != 0:
    s += str(n - 1) + ' '
if (n) % 8 != 0:
    s += str(n + 1) + ' '
if n < 57:
    s += str(n + 8)
print(s)