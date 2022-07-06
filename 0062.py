k = input()
print('BLACK') if (ord(k[0:1])+int(k[1:2]))%2==0 else print('WHITE')