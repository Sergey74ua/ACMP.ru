n = int(input())
a = list(input().split())
m = int(input())
for i in range(m):
    l, r = map(int, input().split())
    s = []
    for j in range(l-1, r):
        s.append(a[j])
    print(*s)