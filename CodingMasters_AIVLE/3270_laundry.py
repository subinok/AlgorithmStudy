# 3270. 빨래 널기
# 옷걸이에는 상의, 하의 구분 없이 빨래를 널 수 있지만 바지 걸이에는 하의 빨래만 널 수 있음
# 상의/하의 빨래 개수가 주어지고, 옷걸이/바지걸이 개수가 주어질때 빨래를 모두 널 수 있는 지를 판단 후 출력

shirt, pants = map(int, input().split())
uhanger, dhanger = map(int, input().split())

if (dhanger - pants) >= 0:
    if (uhanger - shirt) >=0:
        print('YES')
    else:
        print('NO')
else:
    remains = pants - dhanger + shirt
    if (uhanger - remains) >=0:
        print('YES')
    else:
        print('NO')