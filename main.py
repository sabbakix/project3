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
    
    def getCard(self,index):
        return self.hand.pop(index)
    
    def __str__(self):
        if len(self.hand)>0:
            cardstr = ""
            for card in self.hand:
                if card.valuename == "Q":
                    cardstr += " ["+str(card)+"]"
                else:
                    cardstr += " ["+str(card)+"]"
            return self.name+" hand is:\t\t "+cardstr
        else:
            return self.name+" has no more cards."

    def printHand(self):
        cardstr = ""
        i = 0
        for card in self.hand:
            cardstr += " ["+str(card)+"]"
            i += 1
        return cardstr

    def printHiddenCards(self):
        if len(self.hand)>0:
            cardstr = ""
            i = 0
            for card in self.hand:
                cardstr += " [* * ]"
                i += 1
            return self.name+" hand is:\t\t "+cardstr
        else:
            return self.name+" has no more cards. Congratulation!"

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

    def removePairs(self):
        cards = self.hand
        new_cards_list = []
        i = 0
        j = 0
        while(True):
            #print(str(i)+":"+str(j))
            cardi = cards[i]
            cardj = cards[j]
            if (cardi.value == cardj.value) and (cardi.suit != cardj.suit):
                #print(self.name+" removing"+str(cardi)+" "+str(cardj))
                cards.remove(cardi)
                if i > 0:
                    i -= 1
                cards.remove(cardj)
                if j > 0:
                    j -= 1

            if j < len(cards)-1:
                j += 1
            else:
                j = 0
                if i < len(cards)-1:
                    i += 1
                else:
                    break






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
        print("If the player pick The Queen of Clubs (The Old Maid) he cannot discart any card.")
        print("Then the last player that remain with the Old Maid in his hand lose the game, \n")
        print("and pay the drink!\n")
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
#print(deck1)
#deck1.shuffle()


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
            #print(player.name," [",card,"]")
        else:
            #print("stop")
            break

# Diplay all players hands
#for player in players:
#    print(player)
#print("\n")

# Remove pairs
for player in players:
    player.removePairs()
    #print(player)



# Each player pick a card from previous player and remove duplicate cards.
previous_player = players[n_players-1]
i = 0
while(True):
    print(chr(27)+"[2J") # Clear screen
    # Diplay all players hands
    for player in players:
        if player.name == players[i].name:
            print(player)
        else:
            print(player.printHiddenCards())
            #print(player)

    if len(players[i].hand) == 1 and players[i].hand[0].valuename == "Q":
            print("Game Over.\n Sorry "+players[i].name+" You lost.")
            exit()

    print("")
    print(" Hello "+ players[i].name+" is your turn.")
    #print(" Your hand is :"+players[i].printHand()+"\n")

    #print(" "+previous_player.printHiddenCards()+"\n")
    picked = getInput(" Pick a card from "+previous_player.name+
        ". Type a number from 1 to "+str(int(len(previous_player.hand)))+": ")
    try:
        picked = int(picked)-1

    except:
        picked = int(getInput(" Pick a card from "+previous_player.name+
        ". Type a number from 1 to "+str(int(len(previous_player.hand)))+
        ". Please insert a valid number: "))-1

    #remove the card from previous player and add it to me
    picked_card = previous_player.getCard(picked)
    players[i].add(picked_card)


    print("\n You picked: ["+str(picked_card)+"]")
    #check if you have pairs and remove them
    n1_cards = len(players[i].hand)
    players[i].removePairs()
    n2_cards = len(players[i].hand)
    if n1_cards > n2_cards:
        if n2_cards == 0:
            print(" Congratulation, you have no more card!")
        else:
            print(" Congratulation, you removed a pair of cards!")
    else:
        print(" Sorry no card has been removed.")
    
    print(" Your hand is now :"+players[i].printHand()+"\n")    

    # set counters
    previous_player = players[i]
    i += 1
    if i >= n_players:
        i = 0
    pause = getInput(" Press ENTER to continue with the next player: "+players[i].name)