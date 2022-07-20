s = input().split('.')
r = ''
for i in s:
	x = i.split()
	x = x[::-1]
	r += ' '.join(x)
	r += '. '
print(r[:-2])

# Задача вне списка
