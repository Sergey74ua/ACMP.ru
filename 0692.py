x = int(input())
res = 'NO'
test = 1
while x >= test:
    test *= 2
    if x == test or x == 1:
        res = 'YES'
        break
print(res)