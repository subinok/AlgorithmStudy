# 3266. 건물번호
# 건물 번호는 왼쪽에 홀수, 오른쪽에 짝수가 부여됨
# 건물 번호가 주어질 때 이 건물이 왼쪽에 있는지 오른쪽에 있는지 판단

n = int(input())

for i in range(n):
    m = int(input())
    if m%2:
        print('L')
    else:
        print('R')