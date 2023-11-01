n = int(input())

def nod(a, b):
    while a!=0 and b!=0:
        if a>b:
            a=a%b
        else:
            b=b%a
    return(a+b)

s=0
for i in range(1, n):
    if nod(i, n)==1:
        s+=1

print(s)