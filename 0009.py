n = int(input())
arr = list(map(int, input().split()))

mini = 101
maxi = -101
s = 0

for i in range(n):
    if arr[i] > 0:
        s+=arr[i]
    if arr[i] < mini:
        mini = arr[i]
        left = i
    if arr[i] > maxi:
        maxi = arr[i]
        right = i
left, right = min(left, right), max(left, right)

p = 1
for i in range(left+1, right):
    p*=arr[i]

print(s, p)
