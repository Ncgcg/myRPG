from objects import *

# TORY ---------------------------------------------------------------------------------------  
class Story():
    def __init__(self, intro=True):
        self.intro = intro
    
    def menu():
        line()
        print(' 1: > NEW GAME ')
        print(' 2: > LOAD GAME')
        print(' 3: > QUIT     ')
        line()
    
    def intro_story(self):
        line()
        delprint('A few weeks ago, a giant wolf started to kill animals and people in your home village.\n')
        input('')
        delprint("People gathered to dicide who is going to take a try on killing horrifying beast. \nIt appears, they don't like you the most.\n")
        input('')
        delprint('Will you make this attempt by going into a dark forest or reject request in front of not hostile folk?\n')
        line()
        self.intro_choise = input('1: Accept\n2: Reject\n')
    
        if self.intro_choise == '1':
            line()
            delprint('So after some time, you take an old axe and entering the woods.\n')
            input('')
            delprint("It's getting darker and darker. You can hear something close to you.\n")
            input('')
            delprint('A big wild creature seems to be injured. Maybe you have a chance?\n')
            line()
            
        if self.intro_choise == '2':
            line()
            delprint('Next day, while you were choping logs, you can hear omnious wild sounds.\n')
            input('')
            delprint('A Darewolf is injured. Maybe you have a chance?\n')
            line()
            
    
    def cult(self):
        input('')
    
    def retu(self):
        input('')     
             
    def lor(x):
        lor = {1:'What is this', 2:'Does it even work?'}
        print(lor[x])
    