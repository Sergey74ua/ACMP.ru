N = int(input())
m = 0
p = -2
for i in range(N):
    V, S = input().split()
    if (int(S) == 1 and int(V) > m):
        m = int(V)
        p = i
print (p+1)