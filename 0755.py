A, B, C = map(int, input().split())
S = A + B - C
if S >= 0:
    print(S)
else:
    print('Impossible')