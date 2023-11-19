n,k=map(int, input().split())
s=input()
arr=[0]*128
v=r=0
for l in range(n):
    while r<n and arr[ord(s[r])]<k:
        arr[ord(s[r])]+=1
        r+=1
    arr[ord(s[l])]-=1
    v+=(r-l)
print(v)
