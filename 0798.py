m, n, i, j, c = map(int, input().split())
if (n*m)%2==0:
    print('equal')
elif (i%2==j%2 and c==1) or (i%2!=j%2 and c==0):
    print('white')
else:
    print('black')