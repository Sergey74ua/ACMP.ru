w,h=map(int,input().split())
arr1=[]
for i in range(h):
    arr1.append(list(map(int,input())))
arr2=[]
for i in range(h):
    arr2.append(list(map(int,input())))
log=list(input())
arr = [[0]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        if arr1[i][j]==0 and arr2[i][j]==0:
            arr[i][j]=log[0]
        elif arr1[i][j]==0 and arr2[i][j]==1:
            arr[i][j]=log[1]
        elif arr1[i][j]==1 and arr2[i][j]==0:
            arr[i][j]=log[2]
        elif arr1[i][j]==1 and arr2[i][j]==1:
            arr[i][j]=log[3]
for i in range(h):
    print(''.join(arr[i]))
