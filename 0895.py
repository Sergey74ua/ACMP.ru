arr=[]
res='Draw'
for i in range(3):
    arr.append(list(input()))
    if arr[i][0]==arr[i][1]==arr[i][2]=='X':
        res='Win'
    elif arr[i][0]==arr[i][1]==arr[i][2]=='O':
        res='Lose'
for i in range(3):
    if arr[0][i]==arr[1][i]==arr[2][i]=='X':
        res='Win'
    elif arr[0][i]==arr[1][i]==arr[2][i]=='O':
        res='Lose'
if arr[0][0]==arr[1][1]==arr[2][2]=='X':
        res='Win'
elif arr[0][0]==arr[1][1]==arr[2][2]=='O':
        res='Lose'
elif arr[0][2]==arr[1][1]==arr[2][0]=='X':
        res='Win'
elif arr[0][2]==arr[1][1]==arr[2][0]=='O':
        res='Lose'
print(res)