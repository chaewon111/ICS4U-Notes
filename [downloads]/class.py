import random

# 캐릭터 기본 클래스
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp = self.hp -damage
        print(f"{self.name} took {damage} damage! HP left: {self.hp}")

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} attacks {other.name} for {damage} damage!")
        other.take_damage(damage)

# Player 클래스 (Character를 상속)
class Player(Character):
    def heal(self):
        heal_amount = random.randint(5, 10)
        self.hp += heal_amount
        print(f"{self.name} heals for {heal_amount} HP. Current HP: {self.hp}")

# Monster 클래스 (Character를 상속)
class Monster(Character):
    pass

# 게임 시작
player = Player("Hero", hp=30, attack_power=10)
monster = Monster("Goblin", hp=20, attack_power=6)

print("=== Battle Start! ===")

# 전투 루프
while player.is_alive() and monster.is_alive():
    action = input("Choose action (attack/heal): ")

    if action == "attack":
        player.attack(monster)
    elif action == "heal":
        player.heal()
    else:
        print("Invalid action!")

    if monster.is_alive():
        monster.attack(player)

print("=== Battle Over ===")
if player.is_alive():
    print("You won!")
else:
    print("You lost...")
