n, s = map(int, input().split())
s-=1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

r = 0
queue = [s]
friend = [s]
while(len(queue)>0):
    for i in range(n):
        if array[queue[0]][i] and i not in friend:
            friend.append(i)
            queue.append(i)
            r-=-1
    queue.pop(0)

print(r)
