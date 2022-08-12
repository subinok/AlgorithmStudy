# 3274. 코카콜라 맛있다
# 주문의 길이에 따라 메뉴를 정하여 메뉴 출력

order = int(input())
menu = ['jjamppong', 'jjajangmyeon', 'bokkeumbap', 'jjajangmyeon']

print(menu[(order%4 - 1)])