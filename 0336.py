n=l=r=1
for i in input():
    if i == '1':
        n+=1
    else:
        n-=1
    l=min(l, n)
    r=max(r, n)
if l<1:
    r=r+(-l)+1
print(r)