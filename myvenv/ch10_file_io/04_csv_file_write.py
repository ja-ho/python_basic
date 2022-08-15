import csv

data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3, 8],
    ["형돈", 5, 32]
]
# 윈도우의 경우는 csv 파일이 자동으로 한줄 띄어지게 됨 그걸 막기 위해 newline="" 추가
# encoding="utf-8-sig"도 윈도우에서만
file = open("./myvenv/ch10_file_io/student.csv", "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()