# 미래 도시

INF = int(1e9) # 무한을 의미하는 값으로 10억 설정, 1e9는 실수로 취급되어 int() 적용

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j]=0

# 간선 입력 값 적용 -> 양방향, 1의 시간으로 이동
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 간선을 탐색하며 각 노드간 최소 거리 도출 -> 플로이드 워셜 알고리즘
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

dist = graph[1][x]+graph[x][k]

# 도달할 수 없는 경우 -1 출력
if dist >= INF:
    print("-1")
else:
    print(dist)