N=int(input())
arr=[0]
s=0
for i in range(1, N):
    arr.append(i+arr[i-1]+arr[i-1])
print(arr[N-1])

#3-4, 4-11
