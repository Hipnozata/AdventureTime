class Warrior:
    name = "Warrior"
    class ability:
        def __init__(self, name, damage, cooldown, cost):
            self.name = name
            self.damage = damage
            self.cooldown = cooldown
            self.cost = cost
    hp = 200
    atk = 100
    deff = 100
    source = 100
    source_regen = 5
    abilities=[]
    abilities.append(ability('Smash', 5, 0, 0))
    abilities.append(ability('Heroic Bash', 15, 1, 25))
    abilities.append(ability('Gigantual Smash', 25, 3, 40))

class Rogue:
    name = 'Rogue'
    class ability:
        def __init__(self, name, damage, cooldown, cost):
            self.name = name
            self.damage = damage
            self.cooldown = cooldown
            self.cost = cost
    hp = 150
    atk = 100
    deff = 100
    source = 100
    source_regen = 7
    abilities=[]
    abilities.append(ability('Stab', 6, 0, 0))
    abilities.append(ability('Dagger Strike', 10, 1, 20))
    abilities.append(ability('Swift Hit', 15, 2, 30))

class Wizard:
    name = 'Wizard'
    class ability:
        def __init__(self, name, damage, cooldown, cost):
            self.name = name
            self.damage = damage
            self.cooldown = cooldown
            self.cost = cost
    def init_battle(self):
        self.battle_abilities = self.abilities

    def update_turn(self):
        if(self.source!=100):
            self.source+=self.source_regen
        for i in range (3):
            if(self.battle_abilities[i].cooldown>0):
                self.battle_abilities[i].cooldown-=1
        print("You have " + str(self.hp) + " health, " + str(self.source) + " source left.")
    hp = 100
    atk = 100
    deff = 100
    source = 100
    source_regen = 10
    abilities=[]
    battle_abilities = abilities
    abilities.append(ability('Ping', 3, 0, 0))
    abilities.append(ability('Frost Bolt', 15, 2, 30))
    abilities.append(ability('Pyroblast', 30, 5, 60))

characters=[]
characters.append(Warrior)
characters.append(Rogue)
characters.append(Wizard)
Boss1 = Warrior()

def battle(Player, Enemy):
    turn = 0
    Player.init_battle(Player)
    while(Enemy.hp>0):
        Player.update_turn(Player)
        event = int(input("Which ability do you want to use?"))
        print("You casted " + Player.battle_abilities[event-1].name)
        Enemy.hp -= Player.battle_abilities[event-1].damage
        Player.source -= Player.battle_abilities[event-1].cost
    print("GG")
        


def game_welcome():
    print("Hello!")
    name = input("\n\nState your name!\n")
    print("Greetings " + name)
    print("\n\nChoose your class:\n\n", "1. Warrior", "2. Rogue", "3. Wizard", sep='\n')
    character = int(input()) - 1
    print("\n\nYou have chosen " + characters[character].name)
    print("\n\nNow it's time for your first battle!")
    battle(characters[character], Boss1)

game_welcome()    