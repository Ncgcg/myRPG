from text import *
from objects import *
from battle import *

menu = True

while menu:
    Story.menu()
    choise = input('')
    if choise == '1':
        story = Story()
        break
    elif choise == '2':
        pass
    elif choise == '3':
        quit()

while story.intro:
    story.intro_story()
    player = Player()         
    darewolf = Creature('Darewolf', hp = 5, maxhp=10, exp = 4)
    b1 = Battle(player, darewolf)
    b1.battle()
    
    if b1.result == 'creature_esc':
        story.cult()
        cultist = Creature('Cultist', hp = 3, mana=1, exp = 10)
        b2 = Battle(player, cultist)
        b2.battle()
    if b1.player == 'player_esc':
        story.retu()
        
    story.intro = False    

while True:
    line()
    print('1: Darewolf\n2: Bandit\n3: Bear')
    if player.level >= 5:
        print('4: Chimera')
        
    choise = input("Choise your next target? ").lower()
    if choise == '1':
        darewolf = Creature('Darewolf', hp = 3, exp = 4)
        Battle.battle(player, darewolf)
    if choise == '2':
        quit()

player.info()
quit()
    