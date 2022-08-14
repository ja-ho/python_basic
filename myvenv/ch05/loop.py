#반복문
# data=[]
# for i in range(1, 7):
#     x = int(input(str(i) + "일차 턱걸이 횟수>>>"))
#     data.append(x)

# 시퀀스 자료형
# 순서가 있는 자료형

#1. 리스트
#2. 문자열
#3. range 객체
#4. tuple
#5. dictionary

#for 문
# - 리스트 사용
champions = ["티모", "이즈", "리신"]

for champion in champions:
    print(champion)

# - 문자열 사용
message = "화이팅!"

for word in message:
    print(word)

# - range 객체 사용
# range(10) -> -=0~9까지 숫자 포함 range 객체
# range(시작, 끝 + 1)
for i in range(1, 10):
    print(i)
# range(시작, 끝 +1, 단계)

