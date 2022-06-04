# 성적이 낮은 순서로 학생 출력하기
n = int(input())

arr = []
for _ in range(n):
    name, score = input().split()
    arr.append((name, int(score)))

# key를 사용하여 정렬 시 람다 함수 사용
arr.sort(key=lambda x: x[1])

for i in range(n):
    print(arr[i][0], end=' ')