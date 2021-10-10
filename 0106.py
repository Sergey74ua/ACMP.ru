N = int(input())
S = 0
for i in range(N):
    S += int(input())
if (N - S) > S:
    print(S)
else:
    print(N - S)