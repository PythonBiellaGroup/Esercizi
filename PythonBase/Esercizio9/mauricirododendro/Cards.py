"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

and some code by Maria Teresa Panunzio -PythonGroupBiella
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
    rank_names = [  "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    def cmp(self, other):
        
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1

        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # Ranks are the same... it's a tie
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
      for rank in range(0, 4):
        self.cards.append(Card(suit, rank))
        
        
  def add(self, card):
        """Adds a card to the deck.

        card: Card
        """
        self.cards.append(card)      
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
    
  def deal(self, hands, num_cards=999):
    num_hands = len(hands)
    for i in range(num_cards):
      if self.is_empty():
        break # Break if out of cards
      card = self.pop() # Take the top card
      hand = hands[i % num_hands] # Whose turn is next?
      print("deal",hand)
      hand.add(card) # Add the card to the hand
      
class Hand(Deck):
  def __init__(self,name=""):
    
      self.name=name
      self.cards=[]
   
  def add(self, card):
    self.cards.append(card)    
  def __str__(self):
    s = "Hand " + self.name
    if self.is_empty():
      s += " is empty\n"
    else:
      s += " contains\n"
    return s + Deck.__str__(self)

class CardGame:
  def __init__(self):
    self.deck = Deck()
    self.deck.shuffle()
class OldMaidHand(Hand):

  def remove_matches(self):
    count = 0
    original_cards = self.cards[:]
    for card1 in original_cards:
      for i in { 0,1,2,3}-{card1.suit}:
          match=Card(i,card1.rank)
          if match in self.cards:
              self.cards.remove(card1)
              self.cards.remove(match)
              print("Hand {0}: {1} matches {2}".format(self.name, card1, match))
              count += 1
    return count

class OldMaidGame(CardGame):
  
  def play(self, names):
    # Remove randomly
    import random
    self.deck.remove(Card(random.randint(0,3),random.randint(0,3)))
    # Make a hand for each player
    print(len(self.deck.cards),"cards")
    num_cards_deck=len(self.deck.cards)//2
    print ("num cards deck",num_cards_deck)
    self.hands = []
    
    for name in names:
     
      print(self.hands,"name",name)
    
      self.hands.append(OldMaidHand(name))
    
    # Deal the cards
   
    self.deck.deal(self.hands)
    print("---------- Cards have been dealt")
    
    self.print_hands()

    # Remove initial matches
    
    matches = self.remove_all_matches()
    
    print("---------- Matches discarded, play begins")
    self.print_hands()
    # Play until all n//2 cards are matched
    
    turn = 0
    
    num_hands = len(self.hands)
    print(num_cards_deck)
    while matches < num_cards_deck:
     
      matches += self.play_one_turn(turn)
      turn = (turn + 1) % num_hands

    print("---------- Game is Over")
    self.print_hands()
    
  def remove_all_matches(self):
    count = 0
    for hand in self.hands:
      count += hand.remove_matches()
    return count

  def play_one_turn(self, i):
    if self.hands[i].is_empty():
      return 0
    neighbor = self.find_neighbor(i)
    picked_card = self.hands[neighbor].pop()
    self.hands[i].add(picked_card)
    print("Hand", self.hands[i].name, "picked", picked_card)
    count = self.hands[i].remove_matches()
    self.hands[i].shuffle()
    return count

  def find_neighbor(self, i):
    num_hands = len(self.hands)
    for next in range(1,num_hands):
      neighbor = (i + next) % num_hands
      if not self.hands[neighbor].is_empty():
        return neighbor

  def print_hands(self):
    for hand in self.hands:
      print(hand) 


    
if __name__ == '__main__':
 
     
    game = OldMaidGame()
    
    game.play(["Allen","Jeff","Chris"])
   
   
    
