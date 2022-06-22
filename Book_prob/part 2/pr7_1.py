# 부품 찾기

n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()
# 이진 탐색의 경우 탐색할 리스트가 정렬되어 있어야 하므로, 이 과정에서 연산 횟수가 늘어나게 됨

m = int(input())
mlist = list(map(int, input().split()))

for pm in mlist:
    chk = False
    fst = 0
    lst = n-1

    while fst <= lst:
        mid = (lst + fst) // 2
        if nlist[mid] == pm:
            chk = True
            break
        elif nlist[mid] > pm:
            lst = mid - 1
        else:
            fst = mid + 1

    if chk:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        
# 이진 탐색 외 집합 자료형, 계수 정렬 등의 방법으로도 풀이 가능