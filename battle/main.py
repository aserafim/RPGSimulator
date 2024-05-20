from classes.game import Person, bcolors

magic = [{"name" : "Fire", "cost" : 10, "dmg" : 60},
         {"name" : "Thunder", "cost" : 15, "dmg" : 90},
         {"name" : "Fire", "cost" : 5, "dmg" : 30}]


enemy = Person(460, 65, 60, 34, magic)
player = Person(500, 45, 50, 30, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "ANY ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("============================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1
    print("You chose: ", player.actions[index])
    #print("You choose ", player.get_spell_name(int(index)))

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP: ", enemy.get_hp())

    enemy_choice = 1
    
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for" , enemy_dmg, "points of damage.\nYour HP: ", player.get_hp())
    
    #running = False


