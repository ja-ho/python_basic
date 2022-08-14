# list
# data가 있는 리스트
animals = ["가물치", "호랑이", "사자", "코끼리"]

# data가 없는 리스트
empty = ""

# 2. list 조작
print(animals[2])
print(animals[-1])

animals.append("고라니")


animals[0] = "사슴"
# list data 삭제
del animals[0]
print(animals)

# list slicing

print(animals[1:3])
print(animals[:]) # 전체
print(animals[:3]) # 0~2
print(animals[2:])
print(len(animals))
animals.sort()
animals.sort(reverse=True)
print(animals)