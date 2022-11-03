n, An, An1 = map(int, input().split())
for i in range(n-1):
    An, An1 = An1-An, An
print(An, An1)