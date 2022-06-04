# DFS example

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

def dfs(graph, v, visited):
    if visited[v] == True:
        return False

    print(v, end=' ')
    visited[v] = True

    for i in graph[v]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)