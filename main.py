
from random import randint, shuffle

"""

"""

from random import randint, shuffle


class Card:
    def __init__(self, value = 0, suit = ""):
        self.value = value
        self.valuename = str(value)
        self.suit = suit
        self.suitsymbol = ""
    
    def __str__(self):
        return self.valuename+" "+self.suitsymbol+" "

    def setValue(self,value):
        self.value = value

    def setSuit(self, suit):
        self.suit = suit
        self.suitsymbol = self.suitsymbols[suit]

    def setCard(self, value, suit):
        self.setValue(value)
        self.setSuit(suit)
    
    def getCard(self):
        return self.valuename+" "+self.suitsymbol





