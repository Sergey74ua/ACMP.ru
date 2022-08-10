N, i, j = map(int, input().split())
print(min(abs(i-j)-1, N-abs(i-j)-1))