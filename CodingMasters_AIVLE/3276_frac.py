# 3276. 대분수와 가분수
# 대분수 A와 B분의 C가 입력으로 주어질때, 가분수 D분의 E로 바꾸어 출력
# B와 C는 서로소이며, 출력값 D와 E는 서로소여야 함

a, b, c = map(int, input().split())
a = a * b + c
print(b, a)