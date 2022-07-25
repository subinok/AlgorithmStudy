# 도시 분할 계획

n, m = map(int, input().split())
parent = [0] * (n + 1)
edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a, b, cost = map(int, input().split())
    # 비용 순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

edges.sort()

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, x, y):
    x = findParent(parent, x)
    y = findParent(parent, y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

# 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선
maxEdge = 0

for edge in edges:
    cost, a, b = edge
    if findParent(parent, a) == findParent(parent, b):
        unionParent(parent, a, b)
        result += cost
        maxEdge = cost

print(result-maxEdge)
