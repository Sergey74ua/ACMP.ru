n, d = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, n-1
s = 0

arr.sort()

while left <= right:
    if left == right:
        s += 1
        break
    if arr[left] + arr[right] <= d:
        left += 1
    right -= 1
    s += 1

print(s)
