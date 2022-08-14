import random

def getRandomNumber():
    return random.randint(1,45)

def getLottoNums():
    lottos=[]
    while len(lottos) < 6:
        num = getRandomNumber()
        if num not in lottos:
            lottos.append(num)
    return lottos

lotto= getLottoNums()
lotto.sort()

for i in lotto:
    print(i, end=" ")
