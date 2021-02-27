score1 = input()
score = [int(x) for x in score1]
l = len(score)

s1, s2 = 0, 0

for i in range(0,int(l/2)):
  s1 += score[i]
  s2 += score[i+int(l/2)]

if s1 == s2:
  print("LUCKY")

else:
  print("READY")
