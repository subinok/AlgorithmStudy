# 3251. 자격증 시험
# 자격증을 취득하려면 모든 과목에서 40점 이상, 전과목 평균 60점 이상 득점해야한다. 시험 점수가 주어졌을 때, 자격증 취득 여부를 구하여라.

scores = list(map(int, input().split()))
sum = 0
flag = True

for score in scores:
    if score < 40:
        flag = False        
    sum += score

sum /= 5

if sum < 60 or flag == False:
    print('F')
else:
    print('P')