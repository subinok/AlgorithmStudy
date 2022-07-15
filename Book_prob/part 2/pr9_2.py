# 전보
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m, c = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 저장
graph = [[] for i in range(n+1)]
# 최단거리 테이블 초기화
dist = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    # 노드 x에서 노드 y로 가는 비용 z
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for i in graph[now]:
            cost = distance + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

cnt = 0
max_dist = 0
for d in dist:
    if d != INF:
        cnt += 1
        max_dist = max(max_dist, d)

# 시작 노드는 제외해야 하므로 cnt-1 출력
print(cnt-1, max_dist)