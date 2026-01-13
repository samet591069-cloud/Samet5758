import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.alive = True

    def shoot(self, target):
        if not self.alive:
            return

        damage = random.randint(10, 30)
        target.hp -= damage

        print(f"{self.name} ➜ {target.name} vurdu | Hasar: {damage}")

        if target.hp <= 0:
            target.alive = False
            print(f"💀 {target.name} öldü!")

# Oyuncular
player1 = Player("Oyuncu1")
player2 = Player("Oyuncu2")

# Battle döngüsü
while player1.alive and player2.alive:
    player1.shoot(player2)
    if player2.alive:
        player2.shoot(player1)

print("🏆 Oyun bitti")
