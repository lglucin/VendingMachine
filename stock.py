import datetime
from product import Product
import locale
locale.setlocale( locale.LC_ALL, '' )


class Stock():

	def __init__(self, maxItems):
		self.stock = {}
		self.prices = {}
		self.maxItems = maxItems
		self.numItems = 0

	def addStock(self, incomingStock):
		incomingMenu = incomingStock.getMenu()
		incomingPriceTable = incomingStock.getPrices()
		for p,n in incomingMenu.items():
			if p in self.stock:
				self.addProduct(p, n)
			else:
				self.addNewProduct(p, incomingPriceTable[p], n)


	def addProduct(self, product, qty = 1):
		if product.getExpDate() == None or product.getExpDate() < datetime.datetime.now():
			if self.numItems + qty <= self.maxItems:
				if product.getName() in self.stock:
					self.stock[product.getName()] += qty
				else:
					self.stock[product.getName()] = qty
				self.numItems += qty
			else:
				print("Cannot add " + str(qty) + " more.")  
				print("Can add at most " +str(self.maxItems - self.numItems) + ".")

			return True
		else:
			print(product.getName() + " is expired! Throwing away...")
			return False

	def addNewProduct(self, product, price, qty = 1):
		if product.getName() in self.stock:
			print("Product already exists.")
		else:
			if self.addProduct(product, qty):
				self.prices[product.getName()] = price

	def getMenu(self):
		return self.stock

	def getPriceTable(self):
		return self.prices

	def changePrice(self, pName, price):
		if pName in self.prices:
			self.prices[pName] = price
		else:
			print(pName + "is not a product.")

	def displayMenu(self):
		template = "\t|{0:15}|Qty:{1:10}|Cost:{2:7}|"
		for pName in self.stock:
			print(template.format(pName, str(self.stock[pName]), currencyFmt(self.getPrice(pName))))

	def vend(self, pName):
		if self.remove(pName):
			print("Dispensing " + pName + ".")


	def getPrice(self, pName):
		if pName in self.prices:
			return self.prices[pName]
		print(pName + " is not in stock.")


	def remove(self, pName, qty = 1):
		if pName in self.stock:
			self.stock[pName] -= qty
			if self.stock[pName] <= 0:
				self.stock.pop(pName, None)
			return True
		print(pName + " is not in stock.")
		return False

def currencyFmt(val):
	return str(locale.currency(val, grouping=True))