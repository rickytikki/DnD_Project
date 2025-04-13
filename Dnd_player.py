class Player:
#This Class is for the playable Character in a DnD Campaign#

#the first function initializes the Player with their name, inititive bonus, and level (for now)#
    def __init__(self,name,bonus,lvl):
        self.name = name
        self.bonus = bonus
        self.level = lvl
        self.condition = ""
    
    #sets the players initiative to what they rolled + the bonus they had to start#
    def set_initiative(self, roll):
        self.initiative = roll + self.bonus
    
    def Lvl_Up(self, lvl):
        self.level = lvl
        
    def set_condition(self,status):
        self.condition = status
    
    def Check_Player(self):
        print(self.name)
    