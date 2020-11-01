"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

#from __future__ import print_function, division

import random


class Card:
    """Represents a standard playing card.
    
    Attributes:
      suit: integer 0-3
      rank: integer 1-13---modifica 1-14
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    def cmp(self, other):
        self.rank_names[1]=None
        self.rank_names.append("Ace")

        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1

        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0

    
        

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0

class Deck:
    
  def __init__(self):
    self.cards = []
    for suit in range(4):
      for rank in range(1, 14):
        self.cards.append(Card(suit, rank))
        
  def print_deck(self):
    for card in self.cards:
      print(card)
      
  def __str__(self):
    s = ""
    for i in range(len(self.cards)):
      s = s + " " * i + str(self.cards[i]) + "\n"
    return s
  
  def shuffle(self):
    import random
    rng = random.Random()   # Create a random generator
    rng.shuffle(self.cards) # Use its shuffle method
    
  def remove(self, card):
     if card in self.cards:
       self.cards.remove(card)
       return True
     else:
       return False

  def pop(self):
     return self.cards.pop()
  def is_empty(self):
     return self.cards == []
    
if __name__ == '__main__':
    card1=Card(1, 11)
    card2=Card(1,3)
    if card1< card2:
        print("card1 < card2")
    else:
        print("card1>=card2")
    card3=Card(0,14)
   
    print (Card.rank_names[card3.rank])
    print(Card.suit_names[card3.suit])
    card4=Card(0,13)
    print("if card3  values more than  card4 then 1 follows: ",card3.cmp(card4))
    deck = Deck()
    
    deck.shuffle()

   
    
