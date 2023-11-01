N=input()
arr=[]
s=-1

def f(p, r):
    if not r:
        return 2**(len(N)-p)
    if p==len(N):
        return 1
    t=0
    if arr[p]>4:
        t+=f(p+1, 0)
    if arr[p]>7:
        t+=f(p+1, 0)
    if arr[p]==4 or arr[p]==7:
        t+=f(p+1, 1)
    return t

for i in range(len(N)):
    arr.append(int(N[i]))
    s+=2**i

print(s+f(0, 1))
