#클래스를 사용하는 이유

# champion1_name = "이즈"
# champion1_health =700
# champion1_attack = 70

# print(f"{champion1_name}님 소환사의 협곡에 오신것을 환영합니다.")

# champion2_name = "리신"
# champion2_health =700
# champion2_attack = 70

# print(f"{champion2_name}님 소환사의 협곡에 오신것을 환영합니다.")

# def basic_attack(self):
#     print(f"{self.name} 기본공격 {self.attack")

class Champion:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name}님 소환사의 협곡에 오신것을 환영합니다.")
    
    def basic_attack(self):
        print(f"{self.name} 기본공격 {self.attack}")

ezreal = Champion("이즈", 700, 90)
leesin = Champion("리신", 800, 95)
yasuo = Champion("야스오", 800, 95)
ezreal.basic_attack()
leesin.basic_attack()
yasuo.basic_attack()