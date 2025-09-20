# 브루트 포스
money = 1000 - int(input())

ans = int(1e8)

for c500 in range(2):
    for c100 in range(10):
        for c50 in range(20):
            for c10 in range(100):
                for c5 in range(200):
                    value = (c500 * 500) + (c100 * 100) + (c50 * 50) + (c10 * 10) + (c5 * 5)
                    if money - value >= 0:
                        ans = min(ans, c500 + c100 + c50 + c10 + c5 + (money - value))

print(ans)