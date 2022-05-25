def foldingTest(p):
	q = int(p/2) + 1
	if (p == 1):
		print('YES')
	else:
		for j in range(0, q):
			if (j == q - 1):
				print('YES')
			elif (paperList[j] == paperList[p - j - 1]):
				print('NO')
				break
			else:
				continue

if __name__ == '__main__':
	import sys

	t = int(sys.stdin.readline().strip())

	for i in range(0, t):
		paperList = list(map(int, sys.stdin.readline().strip()))
		p = len(paperList)



		# DQ문제임 .......................