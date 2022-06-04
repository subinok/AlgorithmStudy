# 위에서 아래로
n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

# 내림차순의 경우 'reverse = True'
arr.sort(reverse=True)

# 리스트 내의 원소를 띄어쓰기로 구분하여 출력
for i in range(n):
    print(arr[i], end=' ')