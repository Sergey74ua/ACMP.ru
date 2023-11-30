n = int(input())-1
arr = list(map(int, input().split()))

for i in range(1, n):
    if n%i == 0: #подходящий круг
        s = 0 #число совпадений
        while arr[s%i] == arr[s] and s < n:
            s-=-1
        if s == n: #при заданном круге - все совпадают
            n = i
            break
print(n)
