#상속
# : 클래스들에 중복된 코드를 제거하고 유지보수를
# 편하게 하기 위해서 사용

class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    
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
    def move(self): # method overriding
        print(f"{self.name}이 난다")

wolf = Wolf("wolf", 200, 200)
wolf.move()

shark = Shark("shark", 3000, 400)
shark.move()

dragon = Dragon("dragon", 8000, 800)
dragon.move()