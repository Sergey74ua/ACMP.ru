HH, MM = map(int, input().split(':'))
H, M = map(int, input().split())
print(f'{(HH + H + (MM + M) // 60) % 24:02}' + ':' + f'{(MM + M) % 60:02}')