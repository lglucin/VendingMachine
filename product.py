import datetime

class Product():
	def __init__(self, name, expirationDate = None):
		self.name = name
		self.expDate = expirationDate

	def getName(self):
		return self.name

	def getExpDate(self):
		return self.expDate
