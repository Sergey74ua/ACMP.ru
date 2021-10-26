N = int(input())

S = N
for i in range(1, N//2+1):
    if N % i == 0:
        S += i

print(S)