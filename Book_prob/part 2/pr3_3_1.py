# 파일 오류로 버전 추가
# 1이 될 때까지

n, k = map(int, input().split())
cnt = 0

while True:
    if n == 1:
        break
    elif (n % k) != 0:
        """
        target = n - (n % k)
        cnt += n % k
        n = target
        
        위의 코드를 적용하여 연산 횟수 줄일 수 있음
        다만, 사용 시 n < k 인 경우를 예외로 빼서 계산해야 함
        """
        n -= 1
        cnt += 1
    else:
        n /= k
        cnt += 1

print(cnt)