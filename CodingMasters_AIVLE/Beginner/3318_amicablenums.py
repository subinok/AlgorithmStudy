# 3318. 친화수
# A의 진약수의 합이 B이고, B의 진약수의 합이 A라면 A와 B를 친화수라고 한다. 두 수의 쌍이 주어졌을 때 친화수인지 판별

def findDivSum(x):
    result = 0
    for i in range(1, x):
        if x%i == 0:
            result += i
    return result

a, b = map(int, input().split())
a_div = findDivSum(a)
b_div = findDivSum(b)

if (a_div == b) and (b_div == a):
    print('YES')
else:
    print('NO')