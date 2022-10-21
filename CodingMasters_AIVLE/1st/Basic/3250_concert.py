# 3250. 콘서트
# 오늘의 요일이 주어지고, n일 후에 콘서트가 열린다고 할 때 콘서트가 열리는 요일을 구하시오

weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

n = int(input()) % 7
day = input()

for i, d in enumerate(weekday):
    if d == day:
        if i+n > 6:
            print(weekday[i+n-7])
        else:
            print(weekday[i+n])