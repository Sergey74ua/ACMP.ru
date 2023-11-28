n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
s=list(map(int, input().split()))
p=0
for i in arr:
    x=max(0, min(max(i[0], i[2]), max(s[0], s[2]))-max(min(i[0], i[2]), min(s[0], s[2])))
    y=max(0, min(max(i[1], i[3]), max(s[1], s[3]))-max(min(i[1], i[3]), min(s[1], s[3])))
    p+=x*y
print(p)
