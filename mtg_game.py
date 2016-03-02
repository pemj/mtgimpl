from mtg_card import *

def runGame(p1, p2):
	board = Board("commander")
	azami = Card("Azami: Lady of Scrolls", [SuperTyp.legend], [Typ.creature],
				 ["Wizard", "Human"], [Color.colorless, Color.colorless,
									   Color.blue, Color.blue, Color.blue],
				 "no other azamis", [Color.blue], [Color.blue],
				 "Tap an untapped Wizard you control: Draw a card.", "", "")

	heidar = Card("Heidar, Rimewind Master", [SuperTyp.legend], [Typ.creature],
				  ["Wizard", "Human"], [Color.colorless, Color.colorless, Color.colorless,
										Color.colorless, Color.blue],
				  "no other Heidars", [Color.blue], [Color.blue],
				  "Tap: Return target permanent to its owner's hand. Activate this ability only if you control four or more snow permanents.", "", "")

	player1 = Player(board, p1, [], [], azami)
	player2 = Player(board, p2, [], [], heidar)
	return board

