A, B = map(int, input().split())
nA = A
nB = B
while nA != nB:
    if nA < nB:
        nA += A
    else:
        nB += B
print(nA)