sX, sY = map(int, input().split())
pX, pY = map(int, input().split())
n = int(input())
r = 'NO'
for i in range(n):
    x, y = map(int, input().split())
    if (((sX-x)**2+(sY-y)**2)**0.5)*2 <= ((pX-x)**2+(pY-y)**2)**0.5:
        r = i+1
        break
print(r)