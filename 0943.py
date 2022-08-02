N, M, Y, X = map(int, input().split())
print((Y-1)*M+X-(M+1-X*2)*(Y%2-1)-1)