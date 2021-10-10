L, W, H = map(int, input().split())
print(math.ceil(((L + W) * H * 2) / 16))