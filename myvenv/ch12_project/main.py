import os
import csv

#파일 경로
file_path = "./myvenv/ch12_project/data.csv"

# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    f = open(file_path, "r", encoding="utf-8")
    reader = list(csv.reader(f))
    if reader == "":
        pass
    for data in reader:
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
else:
    # 파일 생성
    f = open(file_path, "w", encoding="utf-8", newline="")
    f.close()
