a = input()
b = input()

if len(a)<len(b): #выбор большего числа(если надо)
    a,b=b,a

s=[0]*(len(a)+len(b)) #произведение

a='0'+a #добавляем 0 в начало до размера таблицы умножения
arr=[[0]*len(a) for _ in range(10)] #таблица умножения большего числа на 0-9 (заполняем нулями)
arr[1]=[int(a[i]) for i in range(len(a))] #число умноженное на 1, т.е. оно само

for i in range(2,10): #дополняем таблицу умноженния на 2-9 (складывая с предыдущим)
    for j in range(len(a)): #просто суммируем
        arr[i][j]=arr[i-1][j]+arr[1][j]
    for j in range(len(a)-1,-1,-1): #переносим остатки
        t=arr[i][j]%10
        arr[i][j-1]+=(arr[i][j]-t)//10
        arr[i][j]=t

for i in range(len(b)): #складываем как как при умножении в столбик
    for j in range(len(a)):
        s[i+j]+=arr[int(b[i])][j]

for i in range(len(s)-1,-1,-1): #переносим остатки
    t=s[i]%10
    s[i-1]+=(s[i]-t)//10
    s[i]=t

for i in range(len(s)-1):
    if s[0]==0: #убираем начальные нули
        s=s[1::]
    else:
        break

print(''.join(map(str, s))) #выводим результат
