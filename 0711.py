n, m=map(int, input().split())
mini=m*1000+1
for i in range(n):
    name=input()
    s=sum(map(int, input().split()))
    if s<mini:
        chemp=name
        mini=s
print(chemp)