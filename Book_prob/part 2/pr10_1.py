# 팀 결성

def unionParents(a, b):
    a = findParents(parents, a)
    b = findParents(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 원소가 속한 집합 찾기
def findParents(parents, x):
    if parents[x] != x:
        findParents(parents, parents[x])
    return parents[x]


n, m = map(int, input().split())
parents = [0] * (n + 1)

for i in range(n+1):
    parents[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        unionParents(b, c)
    else:
        if findParents(parents, b) == findParents(parents, c):
            print('YES')
        else:
            print('NO')