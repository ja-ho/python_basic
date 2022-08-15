#raise Exception
#raise Exception("메시지")


# try:
#     num = int(input("음수를 입력해 주세요 >>> "))
#     if num >= 0:
#         raise Exception("양수는 입력 불가")

# except Exception as e:
#     print("에러 발생!", e)

try:
    num = int(input("음수를 입력해 주세요 >>> "))
    if num >= 0:
        raise ValueError("양수는 입력 불가")
except ValueError as e:
    print("에러 발생!", e)