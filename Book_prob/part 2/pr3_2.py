# 숫자 카드 게임

n, m = map(int, input().split())
globalMax = 0

for _ in range(n):
    data = list(map(int, input().split()))
    localMin = min(data)
    """
    if max(globalMax, localMin) == localMin:
        globalMax = localMin
    - 아래의 코드로 간결화 가능
    """
    globalMax = max(globalMax, localMin)

print(globalMax)