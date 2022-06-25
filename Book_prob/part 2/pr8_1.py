# 1로 만들기

x = int(input())

arr = [-1] * (x+1)
arr[1] = 0

for i in range(2, x+1):
    arr[i] = arr[i - 1] + 1
    # 최소값을 찾기 위해 min()함수 사용하여 비교
    if i%5 == 0:
        arr[i] = min(arr[i], arr[i//5] + 1)
    if i%3 == 0:
        arr[i] = min(arr[i], arr[i//3] + 1)
    if i%2 == 0:
        arr[i] = min(arr[i], arr[i//2] + 1)

print(arr[x])