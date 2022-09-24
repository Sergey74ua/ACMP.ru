s=input()
n=m=0
for i in s:
  if i=='0':
    n+=1
    m=max(m, n)
  else:
    n=0
print(m)