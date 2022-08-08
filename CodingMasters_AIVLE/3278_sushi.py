# 빨간색 접시는 1000원, 파란색 접시는 1500원, 초록색 접시는 2000원, 노란색 접시는 3000원, 검은색 접시는 5000원
# 밥을 다 먹고 난 후 각 색깔의 접시 개수가 주어졌을 때, 얼마를 내야 하는지 출력

dishes = [1000, 1500, 2000, 3000, 5000]

eat = list(map(int, input().split()))

price = 0
for i in range(5):
    price += dishes[i] * eat[i]
    
print(price)