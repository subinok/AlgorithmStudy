# 예제 4-1 상하좌우

n = int(input())
roadList = list(input().split())
# list 없이 input().split()으로 입력 가능

# 순서대로 왼쪽, 오른쪽, 위, 아래
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
moveType = ['L', 'R', 'U', 'D']

x = 1
y = 1
# x, y = 1, 1 간단화 가능

for road in roadList:
    for i in range(len(moveType)):
        if road == moveType[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > n or nx < 1 or ny > n or ny < 1:
                continue
            x = nx
            y = ny
            # x, y = nx, ny 이렇게 간단화 가능

print(y, x)