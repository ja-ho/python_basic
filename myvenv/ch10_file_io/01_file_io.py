# 1. 파일 쓰기

# file = open("./myvenv/ch10_file_io/data.txt", "w", encoding="utf-8")
# file.write("1. 파이썬 공부")
# file.close()

# 2. 파일 추가

# file = open("./myvenv/ch10_file_io/data.txt", "a", encoding="utf-8")
# file.write("\n2. 재밌다~")
# file.close()


# 3. 파일 읽기
file = open("./myvenv/ch10_file_io/data.txt", "r", encoding="utf-8")

# 3.1 파일 전체 읽기
# data = file.read()
# print(data)


# 3.2 파일 한줄 읽기
while True:
    data = file.readline()
    print(data, end="")
    if data == "":
        break

file.close()