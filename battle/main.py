from classes.game import Person, bcolors

magic = [{"name" : "Fire", "cost" : 10, "dmg" : 60},
         {"name" : "Thunder", "cost" : 15, "dmg" : 90},
         {"name" : "Fire", "cost" : 5, "dmg" : 30},]


enemy = Person(460, 65, 60, 34, magic)
print(enemy.generate_spell_damage(1))
print(enemy.generate_spell_damage(2))
print(enemy.generate_spell_damage(0))