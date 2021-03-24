"""

"""

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



class Deck(Card):
    def __init__(self):
        self.suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        Card.__init__(self,1,"Hearts")
        self.listofcards = []
        for suit in self.suits:
            for i in range(1,13):
                x = Card(i, suit)
                self.listofcards.append(x)

    def __str__(self):
        deckstr = ""
        for card in self.listofcards:
            deckstr += " ["+str(card.getCard())+"] " 
        return deckstr
    
    def shuffle(self):
        shuffle(self.listofcards)

    def pop(self):
        return self.listofcards.pop()

class Player:
    def __init__(self, name = "", hand = []):
        self.name = name
        self.hand = []
    
    def getName(self):
        return self.name


deck1 = Deck()
print(deck1)
deck1.shuffle()
print(deck1.pop())
