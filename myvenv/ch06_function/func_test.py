# docstring : 설명문

def printSumAvg(x, y, z):
    """
    세 수의 평균을 구하는 함수 
    """
    total = x + y + z
    avg = total /3
    print(f"합계 : {total} 평균 : {avg}")

printSumAvg(1, 2, 3)