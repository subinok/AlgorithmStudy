# 개미 전사

n = int(input())
k = list(map(int, input().split()))

# DP 테이블 정의
arr = [0] * 101
arr[1] = k[0]
arr[2] = max(arr[1], k[1])

for i in range(3, n+1):
    """
    1. i-1 번째를 털 경우 현재 식량창고를 털 수 없음
    2. i-2 번째를 털 경우 현재 식량창고를 털 수 있음
    두 가지 경우 중 큰 값을 저장
    """
    arr[i] = max(arr[i-2]+k[i-1], arr[i-1])

print(arr[n])