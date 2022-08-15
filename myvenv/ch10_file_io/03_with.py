# with 구문 사용하면 자동으로 file close 해준다.
with open("./myvenv/ch10_file_io/data.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data)