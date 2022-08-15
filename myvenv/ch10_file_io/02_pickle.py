#1. 파이썬 객체를 pickle로 저장하기

# import pickle
# data = {
# 	"목표1" : " 팔굽 100",
# 	"목표2" : " 덤벨 100"
# }

# file = open("./myvenv/ch10_file_io/data.pickle", "wb") # wb는 binary 모드
# pickle.dump(data, file)
# file.close()

# 2. pickle 파일 파이썬으로 가져오기
import pickle
file = open("./myvenv/ch10_file_io/data.pickle", "rb") # rb는 binary 모드
data = pickle.load(file)
print(data)
file.close()