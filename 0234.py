n, m, k = map(int, input().split())
arr=[]
for i in range(k):
    arr.append(list(map(int, input().split())))

mtx=[[0]*(m+2) for _ in range(n+2)]

for i in arr:
    mtx[i[0]][i[1]]='*'
    for y in range(i[0]-1, i[0]+2):
        for x in range(i[1]-1, i[1]+2):
            if mtx[y][x]!='*':
                mtx[y][x]+=1

for i in range(1, n+1):
    s=""
    for j in range(1, m+1):
        if mtx[i][j]==0:
            mtx[i][j]='.'
        s+=str(mtx[i][j])
    print(s)
