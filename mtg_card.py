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

#A zone should have a name and some cards.
class Zone:
	name = ""
	permanents = []

class Card:
	"""A card"""
	name = ""
	typ = []
	subtyp = []
	cost = [(0, Color.colorless)]
	constraints = "" #this is gonna be rough
	color = [Color.colorless]
	color_identity = [Color.colorless]
	text = ""
	owner = Player.player1
	location = Zone
