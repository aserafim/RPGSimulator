import random


class Enemy:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh
        

    def getAtk(self):
        print(self.atkl)


    def getHP(self):
        print(self.hp)
    
enemy1 = Enemy(30, 50)
enemy1.getAtk()
enemy1.getHP()

'''
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for ", dmg, "points of damage.", "Currento HP is ", playerhp)

    if playerhp == 30:
        print("You have low health. You've been teleported to the nearest inn.")
        break
'''