n, s, f = map(int, input().split())
s, f = s-1, f-1
array = []
delta = []
queue = [s]
for i in range(n):
	array.append(list(map(int, input().split())))
	delta.append(100**3+1)
delta[s] = 0
while len(queue) > 0:
	for i in range(n):
		if array[queue[0]][i] > 0 and delta[i] > delta[queue[0]] + array[queue[0]][i]:
			queue.append(i)
			delta[i] = delta[queue[0]] + array[queue[0]][i]
	queue.pop(0)

if delta[f] < 100**3+1:
	print(delta[f])
else:
	print(-1)
