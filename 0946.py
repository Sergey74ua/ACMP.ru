n = int(input())
arr = []
res = []
for i in range(n):
	str = list(map(int, input().split()))
	if str[0] == 1:
		arr.insert(0, str[1])
	elif str[0] == 2:
		arr.append(str[1])
	elif str[0] == 3:
		res.append(arr[0])
		arr.pop(0)
	elif str[0] == 4:
		res.append(arr[len(arr)-1])
		arr.pop(len(arr)-1)
print(*res)