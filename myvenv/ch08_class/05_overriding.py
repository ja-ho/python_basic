# 클래스 변수
# 인스턴스들이 모두 공유하는 변수

import random

class Monster:
    max_num = 1000  # class variable
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1
    def decreaseHealth(self, num):
        self.health -= num

    def getHealth(self):
        return self.health

    def move(self):
        print(f"{self.name}가 달린다!")

class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self): # method overriding
        print(f"{self.name}이 헤엄친다")

class Dragon(Monster):
  
    # constructor overriding
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("breath", "bumping", "flying attack")
    def move(self): # method overriding
        print(f"{self.name}이 난다")
    def skill(self):
        print(f"{self.name} 스킬 사용 {self.skills[random.randint(0,2)]}")

dragon = Dragon("dragon", 8000, 800)
dragon.move()
dragon.skill()
wolf = Wolf("wolf", 300, 200)

print(dragon.max_num)