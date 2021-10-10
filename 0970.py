a1, a2, a3 = map(int, input().split())
if a1 + a2 == a3 or a2 + a3 == a1 or a3 + a1 == a2:
    print('YES')
else:
    print('NO')