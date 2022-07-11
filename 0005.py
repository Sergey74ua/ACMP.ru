n = int(input())
arr1 = []
arr2 = []
for i in input().split():
    if int(i) % 2 > 0:
        arr1.append(i)
    else:
        arr2.append(i)
print(*arr1)
print(*arr2)
if len(arr1) > len(arr2):
    print('NO')
else:
    print('YES')