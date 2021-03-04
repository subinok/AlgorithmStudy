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

"""
def main():
  input_s = input()
  len_s = len(input_s)
  front_s, back_s = input_s[:len_s//2], input_s[len_s//2:]

print(sum(list(map(int, front_s)))) == sum(list(map(inst, back_s)))

"""