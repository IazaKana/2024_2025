lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = [False] * 10
choose = []

def permutation(level):
	if level == 5:
		return

	for i in range(0, 10):
		if check[i] == True:
			continue

		choose.append(lst[i])
		check[i] = True

		permutation(level+1)

		check[i] = False
		choose.pop()