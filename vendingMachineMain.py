from stock import Stock
from product import Product
from vendingMachine import VendingMachine
import locale
locale.setlocale( locale.LC_ALL, '' )


def customerInteraction():
	vm = setupVendingMachine()
	vm.serveCustomer()
	print("Come again!")


def setupVendingMachine():
	vm = VendingMachine(Stock(100))
	cheetoes = Product("Cheetoes")
	cupNoodles = Product("Cup Noodles")
	apple = Product("Apple")
	lays = Product("Lays")
	doritoes = Product("Doritoes")
	gum = Product("Gum")
	vm.stock.addNewProduct(cheetoes, 1.5, 20)
	vm.stock.addNewProduct(cupNoodles, 1, 10)
	vm.stock.addNewProduct(apple, 1.15, 20)
	vm.stock.addNewProduct(doritoes, 1.25, 10)
	vm.stock.addNewProduct(gum, 0.50, 25)
	vm.stock.addNewProduct(lays, 1.50, 15)
	return vm

customerInteraction()

