class Car:
	"""Classe définissant une voiture caractérisée par : 
	- color
	- nb_wheels
	- brand
	- position"""
	
	def __init__(car_constructor):
		"""On définit les attributs"""
		self.color = "black"
		self.nb_wheels = 4
		self.brand = "Tesla"
		self.position = 0
	def get_color(self):
		return self.color
	def set_color(self, x)
		self.color = x
	
