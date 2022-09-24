N=int(input())
arr=['A', 'B', 'C', 'E', 'H', 'K', 'M', 'O', 'P', 'T', 'X', 'Y']
for i in range(N):
  s=input()
  if len(s)==6 and s[0] in arr and s[4] in arr and s[5] in arr and s[1:3].isdigit():
    print('Yes')
  else:
    print('No')