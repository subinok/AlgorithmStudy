# 3260. 맞장구 쳐주기
# 1 이상의 정수 k가 주어질 때, k보다 큰 짝수이면서 2로 한 번 나누면 홀수가 되는 정수 n을 출력

k = int(input())

if k%2:
    i=1
else:
    i=2

while True:
    if (k+i)%4:
        print(k+i)
        break
    else:
        i += 2