# 3271. 문제 만들기
# 각 친구들이 만든 문제의 개수가 주어질 때, 앞으로 몇 문제를 더 만들어야 하는지 출력
# 총 만들어야 하는 문제 개수는 100개이며, 만든 문제가 100문제 이상이라면 문제를 더 만들 필요가 없음

n = int(input())
probs = list(map(int, input().split()))

sum = 0
for prob in probs:
    sum += prob

if sum >= 100:
    print(0)
else:
    print(100-sum)