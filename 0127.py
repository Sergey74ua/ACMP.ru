n = int(input())#вершины
array = []      #таблица смежности
delta = []      #длина пути
queue = []      #очередь

for i in range(n):
    array.append(list(map(int, input().split())))
    delta.append(n**n) #заполняем максимальным значением

s,f=map(int, input().split()) #номера вершин
s-=1
f-=1

delta[s]=0 #путь s-й ячейки равен 0
queue.append(s) #добавяляем индекс в очередь

while(len(queue)>0):    #пока все не пройдем
    t=queue[0]          #берем из очереди индекс вершины
    queue.pop(0)        #стираем верхушку очереди
    for i in range(n):  #обходим все связи вершины
        if array[t][i] and delta[i]>delta[t]+1: #ищем более короткий путь
            delta[i]=delta[t]+1                 #среди ненулевых ячеек смежности
            queue.append(i)                     #в очередь, для дальнейшего исследования

if delta[f]<n**n:
    print(delta[f])
else:
    print(-1)
