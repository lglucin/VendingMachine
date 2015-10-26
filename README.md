Vending Machine Project
===================

Author: Lloyd Lucin
-------------------

Requirements:
-------------
Python 3

To Run
---------
Run `python3 vendingMachine.py`  
Can also run with the python interpreter in order to play with classes.

Files:
------
-  vendingMachineMain.py
  -     A console program that allows one to buy from a vending machine.
-  vendingMachine.py
  -  The class implementation of VendingMachine.
  -  Features include:
    -  Ability to serve the customer, menu display, prompting for credit, purchasing products, stock updating, providing a list of products that are affordable with current credit, vending, and change dispensing.
-  stock.py
  -  The class implementation of Stock.  This refers to the variety of Products within a VendingMachine.
  -  Features include:
    -  Ability to set stock limit, consolidating two stocks, adding new products, adding more of existing products, refusal to add Product if past expiration date, changing prices for products, and product removal.
-  product.py
  -  The class implementation of Product. 
  -   Has two attributes:
    -  Name
    -  Expiration Date

Assumptions:
------------
VendingMachines currently only take US currency cash from pennies to $20 bills.  In addition, they may hold an infinite amount of currency and dispense an infinite amount of change.