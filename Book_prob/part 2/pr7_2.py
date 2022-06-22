# 떡볶이 떡 만들기

n, m = map(int, input().split())
tts = list(map(int, input().split()))
tts.sort()
# sort 하기보다 max값만 찾으면 되므로 max(tts)를 사용하면 좋음

fst = 0
lst = tts[n-1]
chk = True
while fst <= lst:
    mid = (fst + lst) // 2
    sum = 0
    for tt in tts:
        if tt-mid > 0:
            sum = sum + tt - mid
    if sum == m:
        print(mid)
        chk = False
        break
    elif sum < m:
        lst = mid - 1
    else:
        fst = mid + 1
        # 최대한 덜 잘랐을 때가 정답이므로, else의 mid 값을 저장하여 마지막에 출력하는 방법도 가능
if chk:
    print(lst)