from stock import Stock
from product import Product
import locale
locale.setlocale( locale.LC_ALL, '' )

class VendingMachine():

    def __init__(self, stock = Stock(100)):
        self.credit = 0
        self.stock = stock
        self.change = {"20":20, "10":10, "5":5, "1":1, "Q":0.25, "D":0.10, "N":0.05, "P":0.01}

    def serveCustomer(self):
        print("Menu:")
        self.stock.displayMenu()
        self.promptForCredit()
        while True:
            next = input("More [C]redit, make [P]urchase, or [M]enu? (ENTER TO EXIT): ")
            next = next.upper()
            if next == 'C':
                self.promptForCredit()
            elif next == 'P':
                self.purchase();
            elif next == 'M':
                self.stock.displayMenu()
            elif next == "":
                break
            else:
                print("Invalid input.  Please Try Again.")
        if self.getCredit() != 0:
            self.giveChange()


    def displayMenu(self):
        if self.stock != None:
            self.stock.displayMenu()
        else:
            print("No Stock.")

    def promptForCredit(self):
        print("Please add credit. (Cash Only)")
        self.receiveCredit(input("Input Money [20, 10, 5, 1, Q, D, N, P]: "))
        print("Credit: " + currencyFmt(self.getCredit()))
        if self.canBuy(self.getCredit()):
            affordableProducts = self.affordableProducts(self.getCredit())
            print("Products Under " + currencyFmt(self.getCredit()) + ":")
            for i in range(len(affordableProducts)):
                product = affordableProducts[i]
                print("\t[" + str(i + 1) + "]: " + product + ": " +  currencyFmt(self.stock.getPrice(product)))

    def purchase(self):
        if self.canBuy(self.getCredit()):
            print("Products Under " + currencyFmt(self.getCredit()) + ":")
            if self.canBuy(self.getCredit()):
                affordableProducts = self.affordableProducts(self.getCredit())
                while True:
                    for i in range(len(affordableProducts)):
                        product = affordableProducts[i]
                        print("\t[" + str(i + 1) + "]: " + product + ": " +  currencyFmt(self.stock.getPrice(product)))
                    while True:
                        productNum = input("Enter # to purchase: ")
                        if productNum.isdigit():
                            productNum = int(productNum) - 1
                            break
                        else:
                            print("Invalid input. Try again.")
                    if productNum >= 0 and productNum < len(affordableProducts):
                        self.vend(affordableProducts[productNum])
                        break
                    else:
                        print("Invalid input.  Please Try Again.")
        else:
            print("No item affordable with " + currencyFmt(self.getCredit()))

    def receiveCredit(self, input):
        """
        Assumption: Machine can take an infinite amount of credit?
        """
        if input.isalpha():
            input = input.upper()
        if input in self.change:
            self.credit += self.change[input]
        else:
            print(input + " is not acceptable.")


    def canBuy(self, credit):
        return len(self.affordableProducts(credit)) != 0


    def getCredit(self):
        return self.credit


    def affordableProducts(self, credit):
        if self.stock != None:
            priceTable = self.stock.getPriceTable()
            affordableProducts = []
            for k,v in priceTable.items():
                if v <= credit and k in self.stock.getMenu():
                    affordableProducts.append(k)
            return affordableProducts
        else:
            print("No Stock.")


    def vend(self, pName):
        if self.stock != None:
            self.stock.vend(pName)
        else:
            print("No Stock.")
        self.credit -= self.stock.prices[pName]
        self.giveChange()

    def giveChange(self):
        credit = int(self.credit * 100)
        clist = [1, 5, 10, 25, 100, 500, 1000, 2000]
        coinsUsed = [0]*(int(credit) + 1)
        coinCount = [0]*(int(credit) + 1)

        print("Making change for", currencyFmt(credit/100),"requires:")
        print(self.dpMakeChange(clist,credit,coinCount,coinsUsed),"items")
        self.printChange(coinsUsed,credit)


    def dpMakeChange(self,coinValueList,change,minCoins,coinsUsed):
        """
        Adatped from http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
        """
        change = int(change)
        for cents in range(change+1):
            coinCount = cents
            newCoin = 1
            for j in [c for c in coinValueList if c <= cents]:
                if minCoins[cents-j] + 1 < coinCount:
                    coinCount = minCoins[cents-j]+1
                    newCoin = j
            minCoins[cents] = coinCount
            coinsUsed[cents] = newCoin
        self.credit = 0
        return minCoins[change]

    def printChange(self,coinsUsed,change):
        coin = change
        changeList = []
        valToCoin = dict([[v,k] for k,v in self.change.items()])
        while coin > 0:
            thisCoin = coinsUsed[coin]
            print(valToCoin[thisCoin / 100], end=" ")
            coin = coin - thisCoin
        print("")

def currencyFmt(val):
        return str(locale.currency(val, grouping=True))




