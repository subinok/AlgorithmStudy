# 3257. 마법의 수
# n이 주어질 때, n과 3으로 나누어 떨어지는 가장 작은 수를 출력

n = int(input())
tmp = n

if n < 3:
    print(3*n)
else:
    if tmp%3:
        tmp %= 3
        print(tmp*n*3)
    else:
        print(n)