from math import sqrt

N = int(1e6)
result = 0
is_prime = [True for _ in range(N + 1)]
# is_prime[k] 가 true이면 k는 소수임을 나타냄.
# is_prime[k] 가 false이면 k는 소수가 아님을 나타냄.
is_prime[1] = False

for i in range(2, int(sqrt(N)) + 1):
    if is_prime[i]:
        for j in range(2 * i, N + 1, i):
            is_prime[j] = False

for i in range(1, N + 1):
    result += is_prime[i]

print(result)