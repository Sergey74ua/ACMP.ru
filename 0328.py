N = int(input())
S = 0
for i in range(N + 1):
    S += i * (N - i + 1) + (i + N) * (N - i + 1) // 2
    #for j in range(i, N + 1):
    #    S += i + j
##print(N * (N + 1) * (N + 2) // 2)
print(S)