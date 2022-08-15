# constructor(생성자)
# 인스턴스를 만들 때 호출되는 메서드


class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    
    def decreaseHealth(self, num):
        self.health -= num

    def getHealth(self):
        return self.health

# 고블린 인스턴스 생성
goblin = Monster(800, 120, 300)
goblin.decreaseHealth(100)
print(goblin.getHealth())

# 늑대 인스턴스 생성
wolf = Monster(1500, 200, 350)
wolf.decreaseHealth(1000)
print(wolf.getHealth())