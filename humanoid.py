class Humanoid:
    def __init__(self, numlegs=2, numarms=2, humanname):
        self.name = humanname
        self.legs = numlegs
        self.arms = numarms
 
    def getName(self):
        return self.name

    def getLegs(self):
        return self.legs

    def getArms(self):
        return self.arms


