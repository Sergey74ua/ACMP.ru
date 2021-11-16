N = int(input())

i = 0
for k in input().split():
    i += 1
    if int(k) <= 437:
        print('Crash', i)
        i = 0
        break

if i != 0:
    print('No crash')