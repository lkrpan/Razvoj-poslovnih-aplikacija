# Zadaća broj 4

class RPSLS_Error(Exception):
	def __init__(self, code = 000):
		self.errorMessage = None

		self.errorDict = {
			000 : "Error 000 : Unspecified error",
			101 : "Error 101 : Igrač je unio krivu vrijednost u glavnom izborniku.",
			102 : "Error 102 : Igrač je unio krivu vrijednost u igri."
		}

		try:
			self.errorMessage = self.errorDict[code]
		except KeyError:
			self.errorMessage = self.errorDict[000]

		print("\n")
		print("=" * 50)
		print(self.errorMessage)
		print("=" * 50)
		print("\n")