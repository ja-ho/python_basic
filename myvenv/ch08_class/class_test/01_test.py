class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        self.isDropable = True
    def sale(self):
        print(f"[{self.name}] 판매가격은 [{self.price}]")
        return self.price
    def discard(self):
        if(self.isDropable):
            print(f"[{self.name}] 버림")
        else:
            print(f"[{self.name}] 못버림")


class WerableItem(Item):
    def __init__(self, name, price, weight, effect):
        super().__init__(name, price, weight)
        self.effect = effect
    def wear(self):
        print(f"[{self.name}] 을 착용함")
        print(f"{self. effect}")
        self.isDropable = False
    def getEffect(self):
        print(self.effect)

class UsableItem(Item):
    def __init__(self, name, price, weight, effect):
        super().__init__(name, price, weight)
        self.effect = effect
        self.isUsed = False
    def use(self):
        if(not self.isUsed):
            print(f"[{self.name}] 을 사용함")
            print(f"{self. effect}")
            self.isUsed = True
        else:
            print(f"[{self.name}] 이미 사용함")
    def getEffect(self):
        print(self.effect)

# 인스턴스 생성
sword = WerableItem("명검", 500, 200, "평범하게 좋습니다")
sword.discard()
sword.wear()
sword.discard()
sword.sale()

portion = UsableItem("신비한 투명물약", 15000, 0.1, "체력 회복 +300")
portion.discard()
portion.use()
portion.use()
portion.sale()