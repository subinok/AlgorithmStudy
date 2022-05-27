# 큰 수의 법칙

# n은 수열의 길이, m은 더하는 횟수, k는 중복 허용 범위
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
fst = data[n-1]
snd = data[n-2]

# 가장 큰 숫자가 들어갈 수 있는 횟수
cnt = (m // (k+1) * k) + m % (k+1)
maxNum = cnt * fst + (m-cnt) * snd

print(maxNum)