A, B = map(int, input().split())
A, B = min(A, B), max(A, B)
while(B):
    B, A = A%B, B
print(A)