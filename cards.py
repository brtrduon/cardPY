import random

class Card(object):
    def __init__ (self, suit, val):
        self.suit = suit
        self.val = val
        self.isDown = True
    def flip(self):
        self.isDown = not self.isDown
    def display(self):
        print "{} of {}".format(self.val, self.suit)

class Deck(object):
    def __init__ (self):
        self.cards = []
    def buildDeck(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        val = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        for i in suits:
            for j in val:
                card = Card(i, j)
                self.cards.append(card)
    def shuffle(self):
        for h in range (len(self.cards) - 1):
            idx = random.randint(0, len(self.cards) - 1)
            self.cards[h], self.cards[idx] = self.cards[idx], self.cards[h]
    def dealCard(self):
        if len(self.cards) < 1:
            print "No more cards to draw, homes"
        else:
            card = self.cards.pop(0)
            #idx = random.randint(0, len(self.cards) - 1)
            #card = self.cards[idx]
            #self.cards.remove(card)
            return card
            print "There are plenty of cards to go around. Woop woop."

class User(object):
    def __init__ (self, name, pokerface = 0):
        self.name = name
        self.pokerface = pokerface
        self.hand = []
    def draw (self, deck):
        card = deck.dealCard()
        self.hand.append(card)
        self.pokerface += 1
        return self
    def discard (self, card = None):
        if card == None:
            card = self.hand[0]
        self.hand.remove(card)
    def showHand(self):
        for k in self.hand:
            k.display()

newDeck = Deck()
newDeck.buildDeck()
newDeck.shuffle()
me = User("bruh")
me.draw(newDeck).showHand()
print me.pokerface
print "Such a low pokerface level. Sad face"