class PlayerCharacter:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def run(self):
		print("Run")
		return "done"

player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 21)
player2.attack = 500
print(player1.name, player2.age, player2.attack)
print(player2.name, player2.age)
print(player2.run)
