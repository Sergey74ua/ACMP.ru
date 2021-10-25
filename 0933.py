A, B, C, T = map(int, input().split())
if T >= A:
    print(A * B + (T - A) * C)
else:
    print(T * B)
