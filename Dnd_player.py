class Player:

    def __init__(self,name,bonus,lvl):
        self.name = name
        self.bonus = bonus
        self.level = lvl
    
    def set_initiative(self, roll):
        self.initiative = roll + self.bonus
    
    def set_Lvl_Up(self, lvl):
        self.level = lvl
        