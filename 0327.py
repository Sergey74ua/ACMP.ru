K=int(input())

def test(s):
  l=str(f'{s//1000:03}')
  l=int(l[0])+int(l[1])+int(l[2])
  r=str(f'{s%1000:03}')
  r=int(r[0])+int(r[1])+int(r[2])
  return l==r

for i in range(K):
  s=int(input())
  if test(s+1) or test(s-1):
    print('Yes')
  else:
    print('No')