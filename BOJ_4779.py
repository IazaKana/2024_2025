n = int(input())

arr = [-1] * (n + 2)
arr[0] = 0
arr[1] = 1

for i in range(2, n + 1):
	arr[i] = arr[i-1] + arr[i-2]

print(arr[n])

#=================================

def sol(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	return sol(x-1) + sol(x-2)


#=================================

