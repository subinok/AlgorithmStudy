# 3273. 우박 수열
# 우박 수열: 모든 자연수 i에 대하여 a_(i+1) = (a_i)/2 (a_i가 짝수인 경우) or 3*(a_i)+1 (a_i가 홀수인 경우)로 정의
# 우박 수열의 초항 N이 주어질때, 이 우박수열의 항이 처음으로 1이 될 때까지 출력

n = int(input())

while True:
    print(n, end=' ')
    if n == 1:
        break
    elif n%2: # n이 홀수일 경우
        n = 3*n+1
    else: # n이 짝수일 경우
        n = n//2