n=int(input())
arr=list(map(int, input().split()))
#Математичесое решение
v=[[0, 0, 0] for i in range(n+1)]
for i in range(n):
    v[i][0]=v[i-1][0]+arr[i]
    v[i][1]=v[i-1][1]+v[i-1][0]*arr[i]
    v[i][2]=v[i-1][2]+v[i-1][1]*arr[i]
print(v[n-1][2])

'''
#Тупой перебор
s=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            s+=arr[i]*arr[j]*arr[k]
print(s)

#Чуть сокращенный алгоритм
s=0
for i in range(n):
    for j in range(i+1,n):
        t=arr[i]*arr[j]
        for k in range(j+1,n):
            s+=t*arr[k]
print(s)
'''
