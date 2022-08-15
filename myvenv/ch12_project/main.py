import os
import csv
from post import Post

#파일 경로
file_path = "./myvenv/ch12_project/data.csv"

# post 객체를 저장할 list
post_list = []

# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    print("loading posts...")
    f = open(file_path, "r", encoding="utf-8")
    reader = list(csv.reader(f))
    for data in reader:
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
    print("post loading done")
else:
    # 파일 생성
    f = open(file_path, "w", encoding="utf-8", newline="")
    f.close()

for post in post_list:
    print(f"{post.get_id()} {post.get_title()} {post.get_content()} {post.get_view_count()}")