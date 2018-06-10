from events import masterList as EventsMasterList

masterDict={}

class Card:
	legalBanners=["Action", "Person", "Thing", "Person/Thing", "God-Level-Being", "None"]
	legalTraits=["Living", "Flipped"]
	legalTypes=["TU", "GSM", "Σ", "Equip"]
	
	def __init__(self, name, banners, traits, abilites, text, isGo=False, isFree=False, isInstant=False, isInterrupt=False, isPRoGS=False):
		self.name = name
		for i in banners:
			assert i in Card.legalBanners
		self.banners = banners
		for i in traits:
			assert i in Card.legalTraits
		self.traits = traits
		for i in abilites:
			assert i in EventsMasterList
		self.abilites = abilites
		self.text = text
		self.isGo = isGo
		self.isFree = isFree
		self.isInstant = isInstant
		self.isInterrupt = isInterrupt
		self.isPRoGS = isPRoGS
		masterDict[self.name]=self
		
	#This is overly generic, should be overridden by subclasses
	def canBePlayed(self, manager):
		if self.isPRoGS:
			return True
		raise NotImplementedError("Card.canBePlayed is an abstract method")
	
	#Should also be overridden
	def play(self, manager, realm=None):
		raise NotImplementedError("Card.play is an abstract method")

class FieldCard(Card):
	def __init__(self, name, banners, traits, abilites, text, CV, types, ascendsTo=None, isGo=False, isFree=False,
	             isInstant=False, isInterrupt=False, isPRoGS=False, isTargetable=True):
		super(self.__class__, self).__init__(name, banners, traits, abilites, text, isGo, isFree, isInstant, isInterrupt, isPRoGS)
		self.CV = CV
		for i in types:
			assert i in Card.legalTypes
		self.types = types
		self.isTargetable = isTargetable
		#TODO Note: Ascended forms must be added before they are referenced now.
		for i in ascendsTo:
			assert i in masterDict.keys()
		self.ascendsTo = ascendsTo
		self.equips=[]
		self.equippedTo = None
		
class ActionCard(Card):
	def canBePlayed(self, manager):
		if self.isPRoGS:
			return True
		#Cannot play non-inturrpts out of turn
		if not self.isInterrupt and manager.activePlayer!=manager.thisPlayer:
			return False
		#Implicily discoved that this is the active player's card
		if manager.currentTurn.remainingActions>0 or self.isFree:
			return True
		return False