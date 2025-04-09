class Player:

    def __init__(self,name,bonus):
        self.name = name
        self.bonus = bonus
    
    def set_initiative(self, roll):
        self.initiative = roll + self.bonus
        