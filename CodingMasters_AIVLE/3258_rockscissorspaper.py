# 3258. 가위바위보
# 가위바위보 횟수 n와 가위바위보에서 낸 모양을 나타낸 수가 주어질 때, 각각 얻은 점수를 공백으로 구분하여 출력
# 1은 가위, 2는 바위, 3은 보를 뜻하며 가위바위보에서 이길 때 마다 1점 획득

n = int(input())

a_score = 0
b_score = 0

for i in range(n):
    a, b = map(int, input().split())
    if a==b:
        continue
    elif b>a:
        if b == 3 and a == 1:
           a_score += 1
        else:
            b_score += 1 
    else:
        if a == 3 and b == 1:
            b_score += 1
        else:
            a_score += 1

print(a_score, b_score)