from mtg_card import *
import random
import collections
# returns 0 on successful damage
def dealDamage(source, target, amount):
    try:
        target.damage += amount
        return 0
    except AttributeError:
        print("target no longer valid")
        return 1
    except NameError:
        print("target no longer valid")
        return 1
    except ReferenceError:
        print("target no longer valid")
        return 1

# using a double-ended queue, because there is no (idiomatic) way to
# append to the left of an arraylist.
class Library:
	def __init__(self):
		self.cards = collections.deque()
	def addToDeck(self, card):
		if(self.cards.count(card) < 4) or ("Basic" in card.supertype):
			self.cards.append(card)
		else:
			print("Only 4 copies of any card that is not a basic land")

	def placeCardOnTop(self, card):
		self.cards.append(card)
	def placeCardOnBot(self, card):
		self.cards.appendleft(card)
	def shuffle(self):
		random.shuffle(self.cards)

class Graveyard():
	def __init__(self):
		self.cards = collections.deque()
	def placeCardOnTop(self, card):
		self.cards.append(card)	
	discard = placeCardOnTop
	def placeCardOnBot(self, card):
		self.cards.appendleft(card)
	def shuffle(self):
		random.shuffle(self.cards)


class Hand():
	def __init__(self):
		self.cards = []
		self.size= 7 # right in the rulebook
		

class Field():
	def __init__(self):
		self.things = {lands: []}

	
