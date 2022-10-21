# 3275. real escape string
# 주어진 문장의 ', ", \를 \', \", \\로 바꾼 문자열을 출력

text = r'\\' # input()

text = text.replace('\\', '\\\\')
text = text.replace('\'', '\\\'')
text = text.replace('\"', '\\\"')

print(text)