from random import randint, shuffle


class Card:
    def __init__(self, value = 0, suit = ""):
        self.value = value
        self.valuename = str(value)
        self.suit = suit
        self.suitsymbol = ""
        self.suitsymbols = {
                            "Spades":  u"\u2660", # ♠
                            "Hearts":  u"\u2665", # ♥
                            "Clubs":   u"\u2663", # ♣
                            "Diamonds":u"\u2666"  # ♦   
                            }
                            
        self.setValue(value)
        self.setSuit(suit)
    
    def __str__(self):
        return self.valuename+" "+self.suitsymbol+" "

    def setValue(self,value):
        self.value = value
        if(value==1):
            self.valuename = "A"
        elif(value==10):
            self.valuename = "J"
        elif(value==11):
            self.valuename = "Q"
        elif(value==12):
            self.valuename = "K"
        else:
            self.valuename = str(value)

    def setSuit(self, suit):
        self.suit = suit
        self.suitsymbol = self.suitsymbols[suit]

    def setCard(self, value, suit):
        self.setValue(value)
        self.setSuit(suit)
    
    def getCard(self):
        return self.valuename+" "+self.suitsymbol

