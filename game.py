import copy
import time
from os import system

clear = lambda: system('clear')
class Warrior:
    class_name = "Warrior"
    class ability:
        def __init__(self, name, damage, cooldown, cost):
            self.name = name
            self.damage = damage
            self.cooldown = cooldown
            self.cost = cost
    def init_battle(self):
        #Had trouble with shallow copy and deep copy. Beware!
        self.battle_abilities = copy.deepcopy(self.abilities)
        self.battle_hp = self.hp
        self.battle_atk = self.atk
        self.battle_deff = self.deff
        self.battle_source_regen = self.source_regen
        self.battle_source = self.source
    def cast_Player(self, Target):
        print("\nAbilities:")
        for i in range (3):
            print(str(i+1) + ". " + self.battle_abilities[i].name + "| Damage:" + str(self.battle_abilities[i].damage) + " Cooldown:" + str(self.battle_abilities[i].cooldown) + " Cost:" + str(self.battle_abilities[i].cost) + " source")
        event = int(input("\nWhich ability do you want to use?\n"))
        if(event-1 < 0 or event-1 > 2):
            clear()
            print("\nInvalid Ability!\n")
            print(Target.name + " has " + str(Target.battle_hp) + " hp left!")
            print("You have " + str(self.battle_hp) + " health, " + str(self.battle_source) + " source left.")
            self.cast_Player(self, Target)
            return
        if(self.battle_abilities[event-1].cooldown != 0):
            clear()
            print("\nAbility " + self.battle_abilities[event-1].name + " is on cooldown! Wait " + str(self.battle_abilities[event-1].cooldown) + " turns to use it.\n")
            print(Target.name + " has " + str(Target.battle_hp) + " hp left!")
            print("You have " + str(self.battle_hp) + " health, " + str(self.battle_source) + " source left.")
            self.cast_Player(self, Target)
            return
        if(self.battle_source < self.battle_abilities[event-1].cost):
            clear()
            print("\nYou don't have enough resource! (" + str(self.battle_source) + " left)\n")
            print(Target.name + " has " + str(Target.battle_hp) + " hp left!")
            print("You have " + str(self.battle_hp) + " health, " + str(self.battle_source) + " source left.")
            self.cast_Player(self, Target)
            return
        clear()
        print("\nYou casted " + str(event) + ". " + self.battle_abilities[event-1].name + "!")
        Target.battle_hp -= self.battle_abilities[event-1].damage
        print(Target.name + " has " + str(Target.battle_hp) + " hp left!")
        self.battle_abilities[event-1].cooldown = self.abilities[event-1].cooldown + 1
        self.battle_source -= self.battle_abilities[event-1].cost
    def update_turn(Target):
        if(Target.battle_source!=100):
            Target.battle_source+=Target.battle_source_regen
        for i in range (3):
            if(Target.battle_abilities[i].cooldown!=0):
                Target.battle_abilities[i].cooldown -= 1
            #print(str(Target.abilities[i].cooldown) + " ")
        print("You have " + str(Target.battle_hp) + " health, " + str(Target.battle_source) + " source left.")
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
    class_name = 'Rogue'
    class ability:
        def __init__(self, name, damage, cooldown, cost):
            self.name = name
            self.damage = damage
            self.cooldown = cooldown
            self.cost = cost
    def init_battle(self):
        #Had trouble with shallow copy and deep copy. Beware!
        self.battle_abilities = copy.deepcopy(self.abilities)
        self.battle_hp = self.hp
        self.battle_atk = self.atk
        self.battle_deff = self.deff
        self.battle_source_regen = self.source_regen
        self.battle_source = self.source
    def cast_Player(self, Target):
        print("\nAbilities:")
        for i in range (3):
            print(str(i+1) + ". " + self.battle_abilities[i].name + "| Damage:" + str(self.battle_abilities[i].damage) + " Cooldown:" + str(self.battle_abilities[i].cooldown) + " Cost:" + str(self.battle_abilities[i].cost) + " source")
        event = int(input("\nWhich ability do you want to use?\n"))
        if(event-1 < 0 or event-1 > 2):
            clear()
            print("\nInvalid Ability!\n")
            print(Target.name + " has " + str(Target.battle_hp) + " hp left!")
            print("You have " + str(self.battle_hp) + " health, " + str(self.battle_source) + " source left.")
            self.cast_Player(self, Target)
            return
        if(self.battle_abilities[event-1].cooldown != 0):
            clear()
            print("\nAbility " + self.battle_abilities[event-1].name + " is on cooldown! Wait " + str(self.battle_abilities[event-1].cooldown) + " turns to use it.\n")
            print(Target.name + " has " + str(Target.battle_hp) + " hp left!")
            print("You have " + str(self.battle_hp) + " health, " + str(self.battle_source) + " source left.")
            self.cast_Player(self, Target)
            return
        if(self.battle_source < self.battle_abilities[event-1].cost):
            clear()
            print("\nYou don't have enough resource! (" + str(self.battle_source) + " left)\n")
            print(Target.name + " has " + str(Target.battle_hp) + " hp left!")
            print("You have " + str(self.battle_hp) + " health, " + str(self.battle_source) + " source left.")
            self.cast_Player(self, Target)
            return
        clear()
        print("\nYou casted " + str(event) + ". " + self.battle_abilities[event-1].name + "!")
        Target.battle_hp -= self.battle_abilities[event-1].damage
        print(Target.name + " has " + str(Target.battle_hp) + " hp left!")
        self.battle_abilities[event-1].cooldown = self.abilities[event-1].cooldown + 1
        self.battle_source -= self.battle_abilities[event-1].cost
    def update_turn(Target):
        if(Target.battle_source!=100):
            Target.battle_source+=Target.battle_source_regen
        for i in range (3):
            if(Target.battle_abilities[i].cooldown!=0):
                Target.battle_abilities[i].cooldown -= 1
            #print(str(Target.abilities[i].cooldown) + " ")
        print("You have " + str(Target.battle_hp) + " health, " + str(Target.battle_source) + " source left.")
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
    class_name = 'Wizard'
    class ability:
        def __init__(self, name, damage, cooldown, cost):
            self.name = name
            self.damage = damage
            self.cooldown = cooldown
            self.cost = cost
    def init_battle(self):
        #Had trouble with shallow copy and deep copy. Beware!
        self.battle_abilities = copy.deepcopy(self.abilities)
        self.battle_hp = self.hp
        self.battle_atk = self.atk
        self.battle_deff = self.deff
        self.battle_source_regen = self.source_regen
        self.battle_source = self.source
    def cast_Player(self, Target):
        print("\nAbilities:")
        for i in range (3):
            print(str(i+1) + ". " + self.battle_abilities[i].name + "| Damage:" + str(self.battle_abilities[i].damage) + " Cooldown:" + str(self.battle_abilities[i].cooldown) + " Cost:" + str(self.battle_abilities[i].cost) + " source")
        event = int(input("\nWhich ability do you want to use?\n"))
        if(event-1 < 0 or event-1 > 2):
            clear()
            print("\nInvalid Ability!\n")
            print(Target.name + " has " + str(Target.battle_hp) + " hp left!")
            print("You have " + str(self.battle_hp) + " health, " + str(self.battle_source) + " source left.")
            self.cast_Player(self, Target)
            return
        if(self.battle_abilities[event-1].cooldown != 0):
            clear()
            print("\nAbility " + self.battle_abilities[event-1].name + " is on cooldown! Wait " + str(self.battle_abilities[event-1].cooldown) + " turns to use it.\n")
            print(Target.name + " has " + str(Target.battle_hp) + " hp left!")
            print("You have " + str(self.battle_hp) + " health, " + str(self.battle_source) + " source left.")
            self.cast_Player(self, Target)
            return
        if(self.battle_source < self.battle_abilities[event-1].cost):
            clear()
            print("\nYou don't have enough resource! (" + str(self.battle_source) + " left)\n")
            print(Target.name + " has " + str(Target.battle_hp) + " hp left!")
            print("You have " + str(self.battle_hp) + " health, " + str(self.battle_source) + " source left.")
            self.cast_Player(self, Target)
            return
        clear()
        print("\nYou casted " + str(event) + ". " + self.battle_abilities[event-1].name + "!")
        Target.battle_hp -= self.battle_abilities[event-1].damage
        print(Target.name + " has " + str(Target.battle_hp) + " hp left!")
        self.battle_abilities[event-1].cooldown = self.abilities[event-1].cooldown + 1
        self.battle_source -= self.battle_abilities[event-1].cost
    def update_turn(Target):
        if(Target.battle_source!=100):
            Target.battle_source+=Target.battle_source_regen
        for i in range (3):
            if(Target.battle_abilities[i].cooldown!=0):
                Target.battle_abilities[i].cooldown -= 1
            #print(str(Target.abilities[i].cooldown) + " ")
        print("You have " + str(Target.battle_hp) + " health, " + str(Target.battle_source) + " source left.")
    hp = 100
    atk = 100
    deff = 100
    source = 100
    source_regen = 10
    abilities=[]
    abilities.append(ability('Ping', 3, 0, 0))
    abilities.append(ability('Frost Bolt', 15, 2, 30))
    abilities.append(ability('Pyroblast', 30, 5, 60))

characters=[]
characters.append(Warrior)
characters.append(Rogue)
characters.append(Wizard)
Boss1 = Wizard()
Boss1.name = "Target Dummy"

def thanks_for_playing():
    print("\nIt seems that you have reached the latest stage of the game. It will be updated from time to time so keep an eye out for updates. Thanks for playing!")
def game_description():
    print("Welcome to my game! This is an RPG where you are the hero and you can choose between three different classes. Once chosen your class will remain the same for the rest of the game. You will battle various enemies and earn points/experience and gain items in order to become stronger and progress through the levels. As this game is still in development there is no gui at the moment. Use terminal for i/o.")

def battle(Player, Enemy):
    turn = 0
    Player.init_battle(Player)
    Enemy.init_battle()
    while(Enemy.battle_hp>0 and Player.battle_hp>0):
        if(turn!=0):
            Player.update_turn(Player)
        Player.cast_Player(Player, Enemy)
        turn += 1
        if(Enemy.battle_hp <= 0):
            time.sleep(2)
            print("Gratz! You beat your first enemy!")
            thanks_for_playing()


def game_welcome():
    print("Hello!")
    time.sleep(2)
    name = input("\n\nState your name!\n")
    time.sleep(2)
    print("\nGreetings " + name)
    time.sleep(2)
    game_description()
    print("\n\nChoose your class:\n\n", "1. Warrior", "2. Rogue", "3. Wizard", sep='\n')
    character = int(input()) - 1
    print("\n\nYou have chosen " + characters[character].class_name)
    time.sleep(2)
    #Initiate first battle
    print("\n\nNow it's time for your first battle!\n\n Loading... \n\n")
    time.sleep(5)
    clear()
    print(str(name) + " is fighting " + Boss1.name + "!!!\n\n")
    battle(characters[character], Boss1)

game_welcome()    