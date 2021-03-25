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
                if i == 11: # Create only one Queen
                    if suit == "Clubs":
                        x = Card(i, suit)
                        self.listofcards.append(x) 
                else:
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
    
    def hasCards(self):
        if len(self.listofcards) > 0:
            return True
        else:
            return False

class Player:
    def __init__(self, name = "", hand = []):
        self.name = name
        self.hand = []
    
    def getName(self):
        return self.name
    
    def add(self,card):
        self.hand.append(card)
    
    def __str__(self):
        cardstr = ""
        for card in self.hand:
            cardstr += "["+str(card)+"] "
        return self.name+" has "+cardstr

    def printHiddenCards(self):
        cardstr = ""
        for card in self.hand:
            cardstr += "[* * ] "
        return self.name+" has "+cardstr

    def arePair(self, card1 = Card, card2 = Card):
        if (card1.value == card2.value) and (card1.suit != card2.suit):
            return True
        else:
            return False
    
    def removeCard(self,card1 = Card):
        cleanhand = []
        for card_x in self.hand:
            if (card_x.value == card1.value) and (card_x.suit == card1.suit):
                pass
            else:
                cleanhand.append(card_x)
        self.hand = cleanhand

    def removePair(self):
        for card_i in self.hand:
            for card_j in self.hand:
                if self.arePair(card_i,card_j):
                    self.removeCard(card_i)
                    self.removePair() #remove al pairs recurvively till no pairs remain





def getInput(printString):
    inputvalue = input(printString)
    if inputvalue == "--help":
        print(chr(27)+"[2J") # Clear screen
        print("\nOLD MAID RULES:\n")
        print("From the deck only the Queen of Clubs (The Old Maid) is kept,")
        print("the others Queens are removed from the deck.")
        print("Then all remaining cards are distributed to players.")
        print("Each player can only see his own cards.")
        print("Players sort through their cards, making as many pairs as possible, and remove them.")
        print("For example 5 of Clubs and 5 of Hearts, or King of Spades and King of Hearts.")
        print("Cards are discarted in pairs. For example if you have 3 Asses only 2 cards can be discarted")
        print("Then the first player pick a card from the second player, then the second")
        print("player pick a card from the third player and so on.")
        print("If the new card is pair in one player hand, he can remove the pair.")
        print("If the player pick The Queen of Clubs (The Old Maid) he cannot remove discart any card.")
        print("Then the last player that remain with the Old Maid in his hand lose the game.\n")
        while(True):
            r = input("Type (--resume) to continue: ")
            if r=="--resume":
                print(chr(27)+"[2J") # Clear screen
                inputvalue = input(printString)
                return inputvalue
    else:
        return inputvalue
        
    
print(chr(27)+"[2J") # Clear screen

deck1 = Deck()
print(deck1)
deck1.shuffle()


n_players = int(getInput("\nInsert the number of players: "))
players = []
# Create an istance for each player and add it to the players list
for i in range(n_players):
    player_name = getInput("Insert the name for player "+str(i+1)+": ")
    player = Player(player_name)
    players.append(player)

# Distribute the cards to players
while(deck1.hasCards()):
    for player in players:
        if deck1.hasCards():
            card = deck1.pop()
            player.add(card)
            print(player.name," [",card,"]")
        else:
            print("stop")
            break

# Diplay all players hands
for player in players:
    print(player)

print("\n")

# Remove pair

for player in players:
    player.removePair()
    print(player)

