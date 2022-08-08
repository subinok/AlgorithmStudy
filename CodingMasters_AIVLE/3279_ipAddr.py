# IP가 주어졌을 때, 해당 IP가 IPv4 형식인지 IPv6 형식인지 출력

addr = input()

if '.' in addr:
    print('IPv4')
else:
    print('IPv6')