# hangle = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ']

# for i in hangle :
#     print(i)
#     ret = input()
#     if i == ret :
#         continue
#     else:
#         break

# 5.3.4
hangle = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ']

right = 0
wrong = 0

for i in hangle :
    print(i)
    ret = input()
    if i == ret :
        right += 1
    else:
        wrong += 1

print(right, " : ", wrong)