r=''
t=0
for i in input():
    if i=='1':
        r+=chr(t+97)
        t=0
    else:
        t+=1
print(r)