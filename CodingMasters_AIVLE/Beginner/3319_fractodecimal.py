# 3319. 분수를 소수로
# 분자와 분모, 그리고 출력해야할 자릿수 n이 주어질 때 분수를 소수 형태로 바꾸어 출력

import decimal
import math

def irreducible(p, q): # p, q 기약분수화
    while True:
        if math.gcd(p, q) == 1:
            return p, q
        else:
            r = math.gcd(p, q)
            p, q = p//r, q//r

def findStart(x): # 순환마디 시작점 구하기 
    if (x % 2 != 0) and (x % 5 != 0): #순순환소수인 경우
        return 1, x
    tmp = x
    a, b = 0, 0
    while True:
        if tmp%5 == 0:
            tmp /= 5
            a += 1
        elif tmp%2 == 0:
            tmp /= 2
            b += 1
        else:
            if tmp == 1: # 유한소수인 경우
                return 0, 0            
            else: #혼순환소수인 경우
                return max(a, b)+1, tmp
        
def findLength(x): # 순환마디 길이 구하기
    n = 1
    while True:
        if (10**(n)-1)%x == 0:
            return n
        else:
            n += 1

  
p, q = map(int, input().split())
n = int(input())

p, q = irreducible(p, q)
start, a0 = findStart(q)

if start == 0:
    result = decimal.Decimal(str(p))/decimal.Decimal(str(q))
    print(f'{result:.{n}f}')
else:
    l = findLength(a0)
    # print(f'start: {start}, length: {l}')
    fst = str(p/q)[:start+1]
    tmp = str(p/q)[start+1:start+l+1]
    # print(f'first: {fst}, tmp: {tmp}')
    
    result_list = list(fst)
    for i in range(start, n+2):
        result_list.append(tmp[i%l])
    
    if int(result_list[len(result_list) - 1]) >= 5:
        last = len(result_list) - 2
        while True:
            if result_list[last] == '.':
                last -= 1
            elif int(result_list[last]) == 9:
                result_list[last] = '0'
                last -= 1
            else:
                result_list[last] = str(int(result_list[last])+1)
                break
    
    result = "".join(result_list)
    print(result[:-1])
    
    
## ------------- 다른 분 답안 ------------- ##
import decimal

a, b = map(int, input().split())
n = int(input())

decimal.getcontext().prec=n # n자리 정밀도
ans = decimal.Decimal(a)/decimal.Decimal(b)

print(f'{ans:.{n}f}')