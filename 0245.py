n=int(input())
arr=[int(input()) for i in range(n)]
arr.sort()

if n<3:
    s=sum(arr)
else:
    l,r=n-3,n-1
    s=t=arr[r-1]+arr[r]
    while l>=0:
        while arr[l]+arr[l+1]<arr[r]:
            s=max(s, t)
            t-=arr[r]
            r-=1
            t+=arr[l]
            l-=1
        if l>=0:
            t+=arr[l]
            s=max(s, t)
            l-=1
print(s)
