def combination(index, level):
	global choose, arr, k

	if level == 6:
		print(choose)
		for u in choose:
			print(i, end=' ')
		print()
		return

	for i in range(index, k):
		choose.append(arr[i])
		combination(i+1, level+1)
		choose.pop()

while True:
	choose = []
	I = list(map(int, input().split()))

	k = I[0]
	arr = I[1:]
	if k == 0:
		break

	combination(0, 0)
	print()

	