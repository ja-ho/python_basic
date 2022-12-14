# 원화를 입력, 환율 입력 - > 달러값

won = input("원화 금액을 입력하세요 >>>")
dolloar = input("환율을 입력하세요 >>>")

try: # 예외가 발생할 수 있는 코드
    print(int(won) / int(dolloar))
except ValueError as e: # 예외가 발생했을 때 실행되는 코드
    print("문자열 예외가 발생했습니다", e)
except ZeroDivisionError as e:
    print("나누기 0은 불가능합니다", e)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드입니다")
finally: # 파일 닫기 등 리소스 반환 필요한 코드
    print("예외가 발생하든, 하지 않든 실행되는 코드입니다")
print("finish")