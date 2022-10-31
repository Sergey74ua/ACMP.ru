n, m=map(int, input().split())
if n==0 and m>0:
    print('Impossible')
elif m==0:
    print(n, n)
elif n>m:
    print(n, n+m-1)
else:
    print(m, n+m-1)