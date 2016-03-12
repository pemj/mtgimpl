from mtg_helpers import *
from enum import Enum

class SuperTyp(Enum):
	legend = 0
	basic = 1
	snow = 2
	ongoing = 3
	world = 4
	
class Typ(Enum):
	instant = 0
	sorcery = 1
	planeswalker = 2
	land = 3
	artifact = 4
	creature = 5
	enchantment = 6
	tribal = 7

class Color(Enum):
	red = 0
	blue = 1
	green = 2
	white = 3
	black = 4
	colorless = 5

class Phase(Enum):
	untap = 0
	upkeep = 1
	draw = 2
	precombat_main = 3
	combat = 4
	postcombat_main = 5
	end = 6

class GameType(Enum):
	modern = 0
	commander = 1
	standard = 2
	pauper = 3
	vintage = 4
	two_headed_giant = 5 #this one may have to wait

#A zone should have a name and some items (cards, tokens, permanents, etc.
class Zone:
	"""A zone of play"""
	def __init__(self, name):
		self.name = name
		self.tenants = []
		
	def add(self, item):
		self.tenants.append(item)
		item.zone = self

		

class Board:
	def __init__(self, gametype):
		self.players = []
		self.gametype = GameType[gametype]
		self.stack = []
		self.turn = 1
		self.phase = Phase.untap
	def addPlayers(self, *args):
		for arg in args:
			self.players.append(arg)
		

class Player:
	"""A player"""
	def __init__(self, board, name, hand, library, commander): # fill this with a default card?  make optional when I remember this
		
		self.name = name
		self.poison_counters = 0
		self.commandzone = Zone("command")
		if board.gametype == GameType.commander:
			self.commandzone.add(commander)
			commander.zone = self.commandzone
		self.hand = hand
		self.library = library
		self.graveyard = []
		board.players.append(self)
		
		

class Card:
	"""A card"""
	def __init__(self, name, supertypes, types, subtypes, cost, constraints, color, color_identity, text, owner, zone):
		self.name = ""
		self.supertypes = supertypes
		self.typ = types
		self.subtyp = subtypes
		self.cost = cost
		self.constraints = constraints
		self.color = color
		self.color_identity = color_identity
		self.text = text
		self.owner = owner
		self.zone = zone

		def makePermanent(self, newZone, controller, time_counters, fading_counters, loyalty_counters,
						  static_abilities, activated_abilities,
						  triggered_abilities, tap_status, targets,
						  power, toughness, pt_counters, summoning_sickness):
			return Permanent(self, newZone, controller, time_counters, fading_counters, loyalty_counters,
							 static_abilities, activated_abilities,
							 triggered_abilities, tap_status, targets,
							 power, toughness, pt_counters, summoning_sickness)

		def makeSpell(self, newZone, controller, originality, targets, effects):
			return Spell(self, self.zone, newZone, controller, originality, targets, effects)


class Spell(Card):
	"""A spell"""
	def __init__(self, card, newZone, controller, originality, targets, effects):
		super(Spell, self).__init__(card.name, card.supertypes, card.types,
										card.subtypes, card.cost,
										card.constraints, card.color,
										card.color_identity,
										card.text, card.owner, newZone)
		self.controller = controller
		self.originality = originality
		self.targets = targets
		self.effects = effects
		

class Permanent(Card):
	"""A card"""
	def __init__(self, card, newZone, controller, time_counters, fading_counters,
				 static_abilities, activated_abilities,
				 triggered_abilities, tap_status, targets,
				 power, toughness, pt_counters, loyalty_counters,
				 summoning_sickness):
		super(Permanent, self).__init__(card.name, card.types,
										card.subtypes, card.cost,
										card.constraints, card.color,
										card.color_identity,
										card.text, card.owner, card.zone)
		self.controller = controller
		self.time_counters = time_counters
		self.fading_counters = fading_counters
		self.loyalty_counters = loyalty_counters
		self.static_abilities = static_abilities
		self.activated_abilities = activated_abilities
		self.triggered_abilities = triggered_abilities
		self.tap_status = tap_status
		self.targets = targets

		self.power = power
		self.toughness = toughness
		self.pt_counters = pt_counters
		self.damage = 0
		self.summoning_sickness = summoning_sickness



#ppython has multiple inheritance, but we'd have to redefine permanents every time they change state, and that sounds like a pain.
#we have permanents, and permanents may be of any permanent type.  they always have power and toughness, but they don't matter if it's not a creature.
