N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr.reverse()
S = 0
for i in range(M):
    if arr[i] > 0:
        S += arr[i]
print(S)
