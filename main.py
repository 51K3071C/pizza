"""
Title: Pizza Time
Description: Manages pizza orders, checkout, and inventory for a local pizza store
Author: Dustin Fulkerson
Version: 1.0
"""
import order, Checkout, printslow, inventory
from os import system
customer_order = []
while True:
    printslow.slow_type("Welcome to Pizza Time!")
    printslow.slow_type("Select an option below.")
    printslow.slow_type("1. Order")
    printslow.slow_type("2. Checkout")
    printslow.slow_type("3. Inventory")
    printslow.slow_type("4. Exit")
    
    selection = input(">> ")
    if selection == "1":
        customer_order = order.start()
    elif selection == "2":
        if len(customer_order) > 0:
            Checkout.start(customer_order)
        else:
            printslow.slow_type("There is nothing in the cart dumby")
    elif selection == "3":
        printslow.slow_type("Fine, didn't want you here anyway!")
        break
    else:
        printslow.slow_type("Stop being a failure. It is 1, 2, or 3. Not that difficult.")
    system("cls")