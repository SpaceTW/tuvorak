


class Turn:
	phases = {0: "Start of Turn", 1: "Draw", 2: "Discard", 3: "End of Turn", 4:"Next Turn"}
	
	def __init__(self, activePlayer):
		#Current phase should be set internally
		self._currentPhase=0
		self.remainingActions=1
		self.remainingFieldCards=1
		#Active Player should not be set elsewhere.
		self._activePlayer=activePlayer
	
	def getNameOfPhase(self):
		return Turn.phases[self._currentPhase]
	
	def getActivePlayer(self):
		return self._activePlayer
	
	def advancePhase(self):
		'''
		
		:return: True if the turn is now over
		'''
		self._currentPhase += 1
		if self._currentPhase>=2:
			#Disallow further plays in the discard phase. Things should have already been played.
			self.remainingActions = 0
			self.remainingFieldCards = 0
		if self._currentPhase==4:
			return True
		assert self._currentPhase > 0
		assert self._currentPhase < 5
		return False