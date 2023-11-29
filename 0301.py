a, b = map(int, input().split())

maxi = ['']*b
s=a
for i in range(b):
    t=min(9, s)
    maxi[i] = str(t)
    s-=t

mini = ['']*b
s = a-1
for i in range(b-1, -1, -1):
    t=min(9, s)
    mini[i] = str(t)
    s-=t
mini[0]=str(int(mini[0])+1)

print(''.join(maxi), ''.join(mini))
