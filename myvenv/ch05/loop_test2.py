while True:
    ret = int(input())
    if ret == 1:
        print("게임을 시작합니다")
    elif ret == 2:
        print("실시간 랭킹")
    elif ret == 3:
        print("게임을 종료합니다")
        break
    else:
        print("다시 입력해주세요")