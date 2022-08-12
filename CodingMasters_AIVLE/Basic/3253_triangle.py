# 3253. 직각삼각형
# 직각삼각형의 세 변의 길이가 주어졌을 때 직각삼각형의 넓이를 계산

a, b, c = map(int, input().split())

m = max(a, b)
m = max(m, c)

if m == c:
    print(a*b//2)
elif m==b:
    print(a*c//2)
else:
    print(b*c//2)