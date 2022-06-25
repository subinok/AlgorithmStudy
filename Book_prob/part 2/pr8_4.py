# 효율적인 화폐 구성

n, m = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

dp = [10001] * (m + 1)
dp[0] = 0

for i in range(n):
    for j in range(coins[i], m+1):
        # 현재 값과 (현재값-코인)+1 값을 비교하여 작은 값 저장
        dp[j] = min(dp[j], dp[j-coins[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])