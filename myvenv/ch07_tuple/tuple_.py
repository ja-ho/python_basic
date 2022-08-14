# 시퀀스 자료형
# 수정, 추가, 삭제가 불가능한리스트
# 메모리 사용이 효율적
# 읽기만 가능하기 때문에 데이터 손실 염려가 없다. 

# 튜플 = (데이터, 데이터, 데이터)
# 튜플 = 데이터, 데이터, 데이터

a = (3, 4, 5)
b = "패스트", 3, True

c = (30,)
d = 30,

e = ([30, 20, 10]) # list를 tuple로 만들기

f = list(ragne(10))
g = tuple(f)

w = 5, 6, 7
x = list(x)

#패킹과 언팩킹

numbers = 3,4,5 # 패킹
a, b, c = numbers # 언패킹

numbersb = [3, 4, 5]
a,b,c = numbers

a, b = b,a
# 튜플함수
a= 10, 20, 30, 40, 30
a.index(20)
a.count(30)
max(a), min(a)
sum(a)
 