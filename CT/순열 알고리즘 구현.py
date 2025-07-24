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

permutation(0)

# 순서에 상관있게 선택해야 하므도 모든 경우를 살펴보도록 구현
# 모든 경우를 살펴보는 대신에 원소가 중복되어 선택되는 것을 방지하기 위해 check 배열 이용