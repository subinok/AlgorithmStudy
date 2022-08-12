# 3261. 자바와 파이썬
# 자바와 파이썬으로 작성한 프로그램의 수행 시간이 주어질 때, 수행시간이 짧은 프로그램 출력 (단, 같을 경우 자바 출력)

java = float(input().strip('s'))
py = float(input().strip('s'))

if py < java:
    print('PYTHON')
else:
    print('JAVA')