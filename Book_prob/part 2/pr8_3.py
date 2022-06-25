# 바닥 공사

n = int(input())

dp = [0] * 1000
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    # 왼쪽부터 차례대로 덮개를 채운다고 생각하고 점화식 세우기
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[n]%796796)