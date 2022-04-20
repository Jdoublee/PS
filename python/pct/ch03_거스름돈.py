n = 1260 # 입력값
res = 0

coins = [500, 100, 50, 10]

for coin in coins:
	res += n // coin
	n %= coin

print(res)