n=int(input())
arr=list(map(int, input().split()))
m=0
for i in range(n):
    m=max(m, arr[(i-1)%n]+arr[i]+arr[(i+1)%n])
print(m)