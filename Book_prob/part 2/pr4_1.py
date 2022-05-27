# 왕실의 나이트

str = input()
x = ord(str[0]) - ord('a') + 1
y = int(str[1])

steps = [(1, 2), (-1, 2), (2, 1), (-2, 1), (-1, -2), (1, -2), (2, -1), (-2, -1)]
cnt = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    cnt += 1

print(cnt)