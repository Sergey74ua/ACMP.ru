n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = n**2

s,f=map(int, input().split())
s-=1
f-=1
queue = [s]

while(len(queue)>0):
    for i in range(n):
        if arr[queue[0]][i] > 0 and arr[s][i] == n**2:
            arr[s][i]=arr[s][queue[0]]+1
            queue.append(i)
    queue.pop(0)
    print(*queue)
    
if arr[s][f]<n**2:
    print(arr[s][f])
else:
    print(-1)
