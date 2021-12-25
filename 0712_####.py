# ДОРАБОТАТЬ
w, h, n = map(int, input().split())
print((int((w * h * n) ** .5 / max(w, h)) + ((w * h * n) ** .5 % max(w, h) > 0)) * max(w, h))