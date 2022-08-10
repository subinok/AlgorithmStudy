# 3264. 피자 사기
# 반지름이 A cm인 피자 한 개의 넓이와 반지름이 B cm인 피자 C개 넓이의 합을 비교

a, b, c = map(int, input().split())

if a**2 > b**2 * c:
    print('NO')
else:
    print('YES')