# 3317. 오리 농법
# n*n 정사각형 땅이 빈 땅, 작물만 있는 땅, 잡초만 있는 땅으로 이루어져 있다. 가로줄 또는 세로줄을 하나 선택할 경우 잡초 및 작물이 모두 없어진다. 작물은 없애지 않고 최대한 많은 잡초를 없앨 때, 잡초만 있는 땅이 몇 개 남는 지 출력
# 0은 빈 땅, 1은 작물만 있는 땅, 2는 잡초만 있는 땅

n = int(input())
farm = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    farm.append(tmp)

row_plants = [False] * 2 * n
col_plants = [False] * 2 * n

for i in range(n):
    for j in range(n):
        if farm[i][j] == 1:
            row_plants[i] = True
         
for i in range(n):
    for j in range(n):
        if farm[j][i] == 1:
            col_plants[i] = True
            break

for i in range(n):
    if not row_plants[i]:
        for j in range(n):
            farm[i][j] = 0

for i in range(n):
    if not col_plants[i]:
        for j in range(n):
            farm[j][i] = 0
result = 0
for i in range(n):
    for j in range(n):
        if farm[i][j] == 2:
            result += 1

print(result)