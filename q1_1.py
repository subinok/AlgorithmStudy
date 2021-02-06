n = int(input())
sc1 = input()

sc = list(map(int, sc1.split(' ')))

sc.sort()

num, j = 0, 0

while j<n:
  tmp = sc[j]
  if n-(j+1)<tmp:
    j += 1
  else:
    j += tmp;
    num += 1

print(num)