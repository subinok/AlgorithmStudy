# 3316. 에어컨
# 최대한 많은 사람을 만족 시킬 수 있는 목표 온도 찾기

n = int(input())
min_list = []
max_list = []

for i in range(n):
    a, b = map(int, input().split())
    min_list.append(a)
    max_list.append(b)
 
if max(min_list) < min(max_list):
    print(max(min_list))
else:
    nl = [0 for _ in range(30)]
    for i in range(30):
        for j in range(n):
            if (min_list[j] <= i) and (i <= max_list[j]):
                nl[i] += 1

    result = nl.index(max(nl))+1
    print(result)
    
## ------------- 다른 분 답안 ------------- ##
N = int(input())
temp = [list(map(int, input().split())) for _ in range(N)]
temp2 = [0]*32 # 온도 길이의 리스트 선언

for i in range(N):
    l = list(range(temp[i][0], temp[i][1]+1)) # 최소최대 범위 숫자 + 1
    for j in l:
        temp2[j] += 1
        
print(temp2.index(max(temp2)))