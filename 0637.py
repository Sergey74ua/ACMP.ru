n = int(input())
arr = list(map(int, input().split()))
k = int(input())
s = 0
for i in arr:
  s += min(i, k)
print(s)