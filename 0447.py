N = int(input())
S = 1
R = 0
for i in range(1, N+1):
  S *= i
while S > 0 and R == 0:
    R = S % 10
    S //= 10
print(R)