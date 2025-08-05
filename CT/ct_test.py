money = 1000 - int(input())
cnt = 0

# 500
cnt += money // 500
money %= 500

# 100
cnt += money // 100
money %= 100

# 50
cnt += money // 50
money %= 50

# 10
cnt += money // 10
money %= 10

# 5
cnt += money // 5
money %= 5

# 1
cnt += money // 1
money %= 1

print(cnt)