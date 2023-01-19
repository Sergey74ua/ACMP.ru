x1, y1, x2, y2 = map(int, input().split())
xA, yA = map(int, input().split())
if x1==x2:
    print(x1*2-xA, yA)
else:
    print(xA, y1*2-yA)