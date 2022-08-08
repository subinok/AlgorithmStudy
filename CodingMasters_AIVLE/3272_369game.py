# 3272. 369 게임
# 3, 6, 9가 들어가는 숫자 차례에는 수에 들어간 3, 6, 9의 개수만큼 박수를 칠 때, 특정 숫자가 입력되었을 때 해야하는 행동을 출력

n = input()
times = n.count('3')
times += n.count('6')
times += n.count('9')

if times:
    print('clap' * times)
else:
    print(n)