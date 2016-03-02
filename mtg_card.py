from enum import Enum
class Typ(Enum):
	instant = 1
	sorcery = 2
	planeswalker = 3
	land = 4
	artifact = 5
	creature = 6
	enchantment = 7
	tribal = 8

class Color(Enum):
	red = 1
	blue = 2
	green = 3
	white = 4
	black = 5
	colorless = 6

class Player(Enum):
	player1 = 1
	player2 = 2
	player3 = 3
	player4 = 4

#A zone should have a name and some items (cards, tokens, permanents, etc.
class Zone:
	"""A zone of play"""
	name = ""
	tenants = []

	
class Card:
	"""A card"""
	def __init__(self, name, types, subtypes, cost, constraints, color, color_identity, text owner, zone):
		self.name = ""
		self.typ = types
		self.subtyp = subtypes
		self.cost = cost
		self.constraints = constraints
		self.color = color
		self.color_identity = color_identity
		self.text = text
		self.owner = owner
		self.location = zone


class Spell(Card):


class Permanent(Card):


class Creature(Permanent):

#The other types will be handled with the self.typ variable
