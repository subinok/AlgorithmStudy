# 3263. 제로 칼로리
# 음료 100ml당 열량이 4kacl 이하이면 제로 칼로리라고 표기할 수 있을때, 구매한 음료의 용량과 열량이 주어지면 제로칼로리 음료라고 표기할 수 있는 지 출력

n, m = map(int, input().split())

if n >= 25 * m:
    print('YES')
else:
    print('NO')