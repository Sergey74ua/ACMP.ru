x = int(input())

if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
    print('12/09/' + f'{x:04}')
else:
    print('13/09/' + f'{x:04}')