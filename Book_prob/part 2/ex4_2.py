# 시각

n = int(input())
cnt = 0

# 모든 시각의 경우(최대 86,400개)를 세어서 풀이
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            # 매 시각에 '3'이 있는지 string 형태로 변환해서 확인
            if '3' in str(h)+str(m)+str(s):
                cnt += 1

print(cnt)