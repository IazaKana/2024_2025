# top-down
def func(n):
	global arr, dp

	if dp[n] != -1:
		return dp[n]

	best = 0
	for i in range(1, n):
		if arr[n] > arr[i]:
			best = max(best, func(i))

	dp[n] = best + 1
	return dp[n]


N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [-1 for _ in range(N + 1)]

dp[1] = 1

for n in range(1, N + 1):
	func(n)

print(max(dp[1:]))