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
	

class Board:
	def __init__(self, players, gametype):
		self.players = players
		self.gametype = gametype
		self.stack = []
		self.turn = 1
		self.phase = Phase.untap
		

class Player:
	"""A player"""
	def __init__(self, board, name, hand, library, graveyard, commander=""): # fill this with a default card?  make optional when I remember this
		self.name = name
		self.poison_counters = 0
		if board.gametype == GameType.commander:
			self.commandzone = commander
		self.hand = hand
		self.library = library
		self.graveyard = graveyard
		
		

#A zone should have a name and some items (cards, tokens, permanents, etc.
class Zone:
	"""A zone of play"""
	def __init(self, name):
		name = name
		tenants = []

	def add(self, item):
		self.tenants.append(item)
		item.zone = self

	
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
		self.zone = zone

		def makePermanent(self, controller, time_counters, fading_counters,
							 static_abilities, activated_abilities,
							 triggered_abilities, tap_status, targets,
							 power, toughness, pt_counters, damage, summoning_sickness):
			return Permanent(self, self.location, controller, time_counters, fading_counters,
							 static_abilities, activated_abilities,
							 triggered_abilities, tap_status, targets,
							 power, toughness, pt_counters, damage, summoning_sickness)

		def makeSpell(self, newZone, controller, originality, targets, effects):
			return Spell(self, self.location, newZone, controller, originality, targets, effects)


class Spell(Card):
	"""A spell"""
	def __init__(self, card, newZone, controller, originality, targets, effects):
		super(Spell, self).__init__(card.name, card.types,
										card.subtypes, card.cost,
										card.constraints, card.color,
										card.color_identity,
										card.text owner, newZone)
		self.controller = controller
		self.originality = originality
		self.targets = targets
		self.effects = effects
		

class Permanent(Card):
	"""A card"""
	def __init__(self, card, newZone, controller, time_counters, fading_counters,
				 static_abilities, activated_abilities,
				 triggered_abilities, tap_status, targets,
				 power, toughness, pt_counters, damage,
				 summoning_sickness):
		super(Permanent, self).__init__(card.name, card.types,
										card.subtypes, card.cost,
										card.constraints, card.color,
										card.color_identity,
										card.text owner, card.zone)
		self.controller = controller
		self.time_counters = time_counters
		self.fading_counters = fading counters 
		self.static_abilities = static_abilities
		self.activated_abilities = activated_abilities
		self.triggered_abilities = triggered_abilities
		self.tap_status = tap_status
		self.targets = targets
		self.power = power
		self.toughness = toughness
		self.pt_counters = pt_counters
		self.damage = damage
		self.summoning_sickness = summoning_sickness
		
	



#ppython has multiple inheritance, but we'd have to redefine permanents every time they change state, and that sounds like a pain.
#we have permanents, and permanents may be of any permanent type.  they always have power and toughness, but they don't matter if it's not a creature.
