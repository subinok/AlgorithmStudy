import sys

n = int(sys.stdin.readline())
result = 0

if n == 1:
  result = 9
else:
  for i in range(pow(10, n-1), pow(10, n)):
    tmp = i
    while tmp >= 10:
      n1 = tmp%10
      tmp = int(tmp/10)
      n2 = tmp%10
      if not abs(n1-n2) == 1:
        break
      if tmp < 10:
        result += 1

print(result%1000000000)

# 시간 초과