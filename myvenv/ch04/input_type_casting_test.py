# 입력과 형변환


x = input("첫번째 숫자를 입력하세요 >>>")
y = input("두번째 숫자를 입력하세요 >>>")

print(type(x))

#숫자형으로 변환 int()
print( int(x) + int(y) )


x = input("태어난 연도를 입력하세요 >> ")
print(2022 - int(x))