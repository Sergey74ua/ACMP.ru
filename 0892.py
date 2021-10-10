N = int(input())
if N < 1 or N > 12:
    print('Error')
elif N > 2 and N < 6:
    print('Spring')
elif N > 5 and N < 9:
    print('Summer')
elif N > 8 and N < 12:
    print('Autumn')
else:
    print('Winter')