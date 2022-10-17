n=input()
r=m=0
for i in input().split():
  if int(i)>0:
    r+=1
    m=max(m, r)
  else:
    r=0
print(m)