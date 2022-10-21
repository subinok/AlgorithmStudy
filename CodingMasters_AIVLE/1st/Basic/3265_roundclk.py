# 3265. 시계 돌리기
# A초를 가리키고 있는 초침을 돌려 정확히 B초를 가리키려 할 때, 돌릴 때 지나가는 칸수를 최소화하여 출력

a, b = map(int, input().split())

if a > b:
    a, b = b, a
    
if (a+60-b) > (b-a):
    print(b-a)
else:
    print(a+60-b)