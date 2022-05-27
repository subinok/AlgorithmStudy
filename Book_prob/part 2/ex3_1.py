# 거스름돈 구하기

n = int(input())

cnt = 0
coinType = [500, 100, 50, 10]

for coin in coinType:
    cnt += n // coin
    n %= coin

print(cnt)