A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
if A[0]==B[0] and A[1]==B[1] and A[2]==B[2]:
    print('Boxes are equal')
elif A[0]>=B[0] and A[1]>=B[1] and A[2]>=B[2]:
    print('The first box is larger than the second one')
elif A[0]<=B[0] and A[1]<=B[1] and A[2]<=B[2]:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')