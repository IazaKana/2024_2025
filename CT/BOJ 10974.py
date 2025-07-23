def permutation(level):
	global N, choose, check

	if level == N:
		print(*choose)
		return

	for i in range(1, N+1):
		if check[i] == True:
			continue

		choose.append(lst[i])
		check[i] = True

		permutation(level+1)

		check[i] = False
		choose.pop()

N = int(input())
check = [False] * (N + 1)
choose = []

permutation(0)