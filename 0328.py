N = int(input())
S = 0
for i in range(N + 1):
    for j in range(i, N + 1):
        S = S + i + j
print(S)