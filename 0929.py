n = int(input())
print(n // 6 + int(n % 6 > 0) * 7 - n % 6, n * 6)