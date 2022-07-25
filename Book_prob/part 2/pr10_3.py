# 커리큘럼

from collections import deque
import copy

n = int(input())
indegree = [0] * (n + 1)
time = [0] * (n + 1)
graph = [[] for i in range(n+1)]

for i in range(1, n+1):
    t = list(map(int, input().split()))
    time[i] = t[0]
    for j in range(1, len(t)-1):
        graph[t[j]].append(i)
        indegree[i] += 1

def topologySort():
    # 리스트의 경우 대입 연산 시 값이 변경 될 때 문제가 발생할 수 있어 deepcopy() 함수 사용
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topologySort()