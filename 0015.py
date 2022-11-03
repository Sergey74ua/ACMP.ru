n=int(input())
r=0
for i in range(n):
    r+=input().count('1')
print(r//2)