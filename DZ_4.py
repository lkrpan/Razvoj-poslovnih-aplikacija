# Zadaća broj 4

import random
from DZ_4_Error import RPSLS_Error

class RPSLS:
	def __init__(self):
		self.playerInput = None
		self.playerNumber = -1
		self.aiInput = None
		self.aiNumber = -1

	def TitleCard(self):
		print("=======================================================")
		print("======== Rock, paper, scissors, lizard, spock =========")
		print("=======================================================")

	def MainMenu(self):
		print("\n")
		print("[1] Igraj Rock, paper, scissors, lizard, spock.")
		print("[2] Izlaz.")
		print("\n")
		self.playerChoice = int(input("Odaberite šta želite raditi: "))

	def NumToString(self):
		if self.aiNumber == 0:
			self.aiInput = "Rock"
		elif self.aiNumber == 1:
			self.aiInput = "Paper"
		elif self.aiNumber == 2:
			self.aiInput = "Scissors"
		elif self.aiNumber == 3:
			self.aiInput = "Lizard"
		elif self.aiNumber == 4:
			self.aiInput = "Spock"
		else:
			self.aiInput = None
			print("Greška")
		return self.aiInput
	
	def StringToNum(self):
		if self.playerInput == "rock":
			self.playerNumber = 0
		elif self.playerInput == "paper":
			self.playerNumber = 1
		elif self.playerInput == "scissors":
			self.playerNumber = 2
		elif self.playerInput == "lizard":
			self.playerNumber = 3
		elif self.playerInput == "spock":
			self.playerNumber = 4
		else:
			self.playerNumber = -1
			raise RPSLS_Error(102)
		return self.playerNumber
		
	def Play(self):	
		self.TitleCard()
		self.MainMenu()

		while (self.playerChoice != 2):
			playerScore = 0
			aiScore = 0
			
			if(self.playerChoice > 2 or self.playerChoice < 1):
				raise RPSLS_Error(101)
			else:
				while (playerScore < 3 and aiScore < 3):
					print("=" * 50)
					self.playerInput = input("Odaberite jedno od navedenog (Rock/Paper/Scissors/Lizard/Spock): ").lower()
					self.playerNumber = self.StringToNum()

					self.aiNumber = random.randrange(0, 5)

					ostatak = (self.playerNumber - self.aiNumber) % 5

					if(self.playerNumber == -1):
						winner = "Greška"
						raise RPSLS_Error(102)
					else:
						if(ostatak == 0):
							winner = "Nitko, neriješeno je!"
						elif(ostatak == 1 or ostatak == 2):
							winner = "Igrač"
							playerScore += 1
						elif(ostatak == 3 or ostatak == 4):
							winner = "AI"
							aiScore += 1

					self.aiInput = self.NumToString()

					print("=" * 50)
					print("Igrač je odabrao: {}".format(self.playerInput.capitalize()))
					print("AI je odabrao: {}".format(self.aiInput))
					print("=" * 50)
					print("Ovu rundu je dobio: {}".format(winner))
					print("=" * 50)
					print("Igrač ima {} bodova.".format(playerScore))
					print("AI ima {} bodova.".format(aiScore))

					
				if(playerScore == 3):
					print("=" * 50)
					print("Pobjednik igre je Igrač!")
					print("=" * 50)
				elif(aiScore == 3):
					print("=" * 50)
					print("Pobjednik igre je AI!")
					print("=" * 50)
				
				self.MainMenu()

if __name__ == "__main__":
	game = RPSLS()
	game.Play()