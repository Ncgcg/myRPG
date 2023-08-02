import sys,time

# BASIC FUNCTIONS ---------------------------------------------------------------------------
def delprint(text, delay_time=.00): 
  for character in text:      
    sys.stdout.write(character) 
    sys.stdout.flush()
    time.sleep(delay_time)
    
def line():
    print('='*100) 
    
# ATTRIBUTES -----------------------------------------------------------------------------------------
class Attribute():
    def __init__(self, name:str, type:str, attack=0, defence=0, mana=0):
        self.name = name
        self.type = type
        self.attack = attack
        self.defence = defence
        self.mana = mana

knife = Attribute('knife', 'w', attack=3)
sword = Attribute('sword', 'w', attack=5)
mace = Attribute('mace', 'w', attack=10 )
  
lether = Attribute('lether', 'a', defence=1)     
chainmail = Attribute('chainmail', 'a', defence=3)
chield = Attribute('chainmale', 'a', defence=10)       

# CREATURES AND PLAYER -------------------------------------------------------------------------------
class Creature():
    def __init__(self, name:str=None, maxhp=1, hp=1,  mana=0, attack=1, defense=0, exp=0, esc = False):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.maxmana = mana
        self.mana = mana
        self.attack = attack
        self.exp = exp
        self.defense = defense
        self.esc = esc
        
    def simple_attack(self, other):
        if self.hp <= other.attack:
            self.esc = True
        if self.hp > other.attack:
            other.hp -= self.attack
            other.exp += self.attack  
            
    def move(self, other):
        Creature.simple_attack(self, other) 

class Player(Creature):
    def __init__(self, rhand:Attribute=None, lhand:Attribute=None, body:Attribute=None):
        super().__init__()
        self.level = 0
        self.maxhp = 3
        self.hp = 3
        self.attack = 2
        self.rhand = rhand
        self.lhand = lhand
        self.body = body
    
    def info(self):
        line()
        print('EXPIRIENCE -', self.exp, '\nLEVEL - ', self.level)
        print('HEALTH POINTS -', self.hp, '/', self.maxhp)
        if self.maxmana > 0:
            print('MANA -', self.mana, '/', self.maxmana)
        print('ATTACK -', self.attack)
        if self.defense > 0:
            print('DEFENSE - ', self.defense)
        line()
        
    def move(self, other):
        print('What whould you like to do?')
        line()
        print('1: Attack\n2: Run')
        line()
        choise = input('')
        if choise == '1':
            other.hp -= self.attack
            other.exp += self.attack  
        if choise == '2':
            self.esc = True
    
    def level_up(self):
        exp_needed = 10
        increment = 5
        
        if self.level == 0 and self.exp >= exp_needed:
            line() 
            print('UPGRADE!')
            # Create good upgrade benefits
            line() 
            self.exp -= 10
            self.level += 1 
            exp_needed += increment
        
        if self.level == 1 and self.exp >= exp_needed:
            line() 
            print('UPGRADE!')
            print('+5 HP, +1 ATTACK')
            line()
            self.hp += 5
            self.attack += 1 
            self.exp -= 13  
            self.level += 1 
            exp_needed += increment
            
            # Introduce magic
            print('Choise new skills: ') 
            print('1, +10 MANA')
            print('2, Weapon')
            print('3, Armour')
            
bandit = Creature('Bandit', hp = 10, attack = 2, exp = 5)
chimera = Creature('Chimera', hp = 100)
hydra = Creature('Hydra', hp = 1000, attack = 100)


