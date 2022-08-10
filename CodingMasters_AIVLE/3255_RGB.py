# 3255. RGB
# 삼원색 정보를 담고 있는 n * m 배열이 2개 주어질 때, 배열을 합성하여 만든 배열을 출력
# 빨강 + 초록 = 노랑
# 초록 + 파랑 = 청록
# 파랑 + 빨강 = 자홍

color = {'R': [1, 0, 0], 'G': [0, 1, 0], 'B':[0, 0, 1]}
mix = {'Y': [1, 1, 0], 'C': [0, 1, 1], 'M': [1, 0, 1]}

n, m = map(int, input().split())
a = []
b = []

for _ in range(n):
    tmp = list(input().split())
    a.append(tmp)
    
for _ in range(n):
    tmp = list(input().split())
    b.append(tmp)

c = [[None] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            c[i][j] = a[i][j]
        else:
            tmp = [color[a[i][j]][k] + color[b[i][j]][k] for k in range(3)]
            for k, v in mix.items():
                if v == tmp:
                    c[i][j] = k
                    break

for i in range(n):
    for j in range(m):
        print(c[i][j], end=' ')
    print()