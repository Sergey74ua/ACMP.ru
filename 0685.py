A1, A2, A3, B1, B2, B3 = map(int, input().split())
arr1 = [A1, A2, A3]
arr1.sort()
arr2 = [B1, B2, B3]
arr2.sort()
print(arr1[0]*arr2[0] + arr1[1]*arr2[1] + arr1[2]*arr2[2])