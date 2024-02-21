n=int(input())
t=[i for i in range(1,n*n+1)]
r="Correct"

arr=[]
for i in range(n*n):
    s=list(map(int,input().split()))
    arr.append(s)
    v=s
    v.sort()
    print(v)
    if len(s)!=len(set(s)):
        r="Incorrect"
        break

for i in range(n*n):
    v=[]
    for j in range(n*n):
        v.append(arr[j][i])
    if len(v)!=len(set(v)):
        r="Incorrect"
        break

for si in range(n):
    for sj in range(n):
        v=[]
        for i in range((si)*n,(si+1)*n):
            for j in range((sj)*n,(sj+1)*n):
                v.append(arr[i][j])
        if len(v)!=len(set(v)):
            r="Incorrect"
            break

print(r)
