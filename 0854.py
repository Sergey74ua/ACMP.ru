T1, T2 = map(int, input().split())
mode = input()

if mode == 'freeze':
    print(min(T1, T2))
elif mode == 'heat':
    print(max(T1, T2))
elif mode == 'auto':
    print(T2)
elif mode == 'fan':
    print(T1)