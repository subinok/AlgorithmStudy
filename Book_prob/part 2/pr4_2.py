# 게임 개발

n, m = map(int, input().split())
x, y, d = map(int, input().split())

"""
TypeError: '----' object is not callable
이전에 선언한 변수를 함수처럼 사용하려 해서 일어나는 에러로, 함수명으로 쓰이는 단어를 중복하여 사용했을 때 주로 발생함 
같은 이름의 변수가 위에 선언되어 있지는 않은지 확인해야함
"""

# 전체 맵 정보 입력
mapList = []
for i in range(n):
    mapList.append(list(map(int, input().split())))


# 방문한 위치를 저장하기 위한 맵 생성 및 초기화
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def turnLeft(dir):
    dir -= 1
    if dir == -1:
        dir = 3
    return dir


turnTime = 0
cnt = 1
while True:
    d = turnLeft(d)
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] == 0 and mapList[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turnTime = 0
        continue
    else:
        turnTime += 1
    # 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 경우
    if turnTime == 4:
        nx = x - dx[d]
        ny = x - dy[d]
        if mapList[nx][ny] == 0:
            x = nx
            y = ny
            turnTime = 0
        else:
            break

print(cnt)