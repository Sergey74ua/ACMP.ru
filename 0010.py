A, B, C, D = map(int, input().split())
arr = []
for i in range(-100, 100+1):
    if A*i**3+B*i**2+C*i+D==0:
        arr.append(i)
arr.sort()
print(*arr)