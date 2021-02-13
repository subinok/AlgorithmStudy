import sys

t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())
  n1 = [int(sys.stdin.readline()) for i in range(n)]
  n2 = [int(sys.stdin.readline()) for i in range(n)]
  n0 = []
  n0.append(n1)
  n0.append(n2)
  print(n0)

  #list 입력 방법
