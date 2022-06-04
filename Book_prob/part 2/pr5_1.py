# 음료수 얼려 먹기
n, m = map(int, input().split())

iceArr = []
for _ in range(n):
    iceArr.append(list(map(int, input())))

def findIce(i, j):
    if i < 0 or i > n-1 or j < 0 or j > m-1:
        return 0
    if iceArr[i][j] == 1:
        return 0
    else:
        iceArr[i][j] = 1
        findIce(i+1, j)
        findIce(i-1, j)
        findIce(i, j+1)
        findIce(i, j-1)
        return 1

cnt = 0
for i in range(n):
    for j in range(m):
       cnt += findIce(i, j)

print(cnt)