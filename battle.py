from objects import *

class Battle():
    def __init__(self, player:Player, creature:Creature):
        self.player = player
        self.creature = creature
    
    def info(self):
        line()
        print('BATTLE LOG')
        line()
        print('PLAYER', ' '*30, self.creature.name.upper())
        print('HEALTH POINTS -', self.player.hp, '/', self.player.maxhp, ' '*15, 'HEALTH POINTS -', self.creature.hp, '/', self.creature.maxhp,)
        if self.player.maxmana or self.creature.maxmana > 0:
            print('MANA -', self.player.mana, '/', self.player.maxmana, ' '*24, 'MANA -', self.creature.mana, '/', self.creature.maxmana)
        print('ATTACK -', self.player.attack, ' '*26, 'ATTACK -', self.creature.attack, )
        if self.player.defense or self.creature.defense > 0:
            print('DEFENSE - ', self.player.defense, ' '*22, 'DEFENSE - ', self.creature.defense)
        print('EXPIRIENCE -', self.player.exp, ) 
        print('LEVEL - ', self.player.level)
        line()
    
    def battle(self): 
        turn = 0
        self.info()
        while True:
            self.player.move(self.creature)
            if self.player.esc == True:
                print('You have escaped!')
                self.result = 'player_esc'
                break
            if self.creature.hp <= 0:
                line()
                self.player.exp += self.creature.exp
                self.info()
                self.result = 'w'
                print('You won! Nice fight')
                break
            self.creature.move(self.player)
            if self.creature.esc == True:
                self.info()
                print(self.creature.name, 'have escaped!')
                self.result = 'creature_esc'
                break
            if self.player.hp <= 0:
                self.result = 'l'
                print('You lost!')
                quit()
            self.info()
            print('-', self.creature.attack, 'HP')
            line()
            turn +=1 
        self.player.level_up()
           
    # SPELLS AND OBJECTS ---------------------------------------------------------------------------------
    # not ready 
    def bleeding(target):
        pass 
    def curse(performer, target, level):
        if level == '1':
            performer.mana -= 1
            target.hp -= 1
        if level == '2':
            performer.mana -= 2
            target.hp -= 2
        if level == '3':
            performer.mana -= 3
            target.hp -= 3
        
    

     