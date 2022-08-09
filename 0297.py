N=input()
r=0
for i in N:
  if i=='0' or i=='6' or i=='9':
    r+=1
  elif i=='8':
    r+=2
print(r)