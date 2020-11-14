import random
import sys
import math

class Genders:
    Female = 1
    Male = 2

class Animal():
    _ID = 1
    def __init__(self, AvgLifespan, Variability):
        rndValue = self.CalculateRandomValue(100, Variability)
        self.naturalLifespan = int(AvgLifespan * rndValue / 100)
        self.isAlive = True
        self.age = 0
        self._ID = Animal._ID
        Animal._ID += 1
        
    def CalculateRandomValue(self, BaseValue, Variability):
        return BaseValue - (BaseValue * Variability / 100) + (BaseValue * random.randint(0, Variability * 2) / 100)

class Fox(Animal):
    def __init__(self, Variability):
        self.DEFAULT_LIFE_SPAN = 7
        super(Fox, self).__init__(self.DEFAULT_LIFE_SPAN, Variability)
        self.foodUnitsNeeded = int(10 * self.CalculateRandomValue(100, Variability) / 100)
    
    def __repr__(self):
        return "Fox(ID=%s, foodUnitsNeeded=%s, isAlive=%s, age=%s)" % (self._ID, self.foodUnitsNeeded, self.isAlive, self.age)
    
class Rabbit(Animal):
    def __init__(self, Variability):
        self.DEFAULT_LIFE_SPAN = 4
        super(Rabbit, self).__init__(self.DEFAULT_LIFE_SPAN, Variability)
        if random.randint(0, 100) < 50:
            self.gender = Genders.Male
        else:
            self.gender = Genders.Female

    def __repr__(self):
        return "Rabbit(ID=%s, gender=%s, isAlive=%s, age=%s)" % (self._ID, self.gender, self.isAlive, self.age)