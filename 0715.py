n, m = map(int, input().split())
arr=[]
r=0
for i in range(n):
    arr.append(input())
input()
for i in range(n):
    s=input()
    for j in range(m):
        if arr[i][j] == s[j]:
            r+=1
print(r)