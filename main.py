"""
Title: Pizza Time
Description: Manages pizza orders, checkout, and inventory for a local pizza store
Author: Dustin Fulkerson
Version: 1.0
"""
import order, Checkout, printslow, inventory
printslow.slow_type("Welcome to Pizza Time!")
printslow.slow_type("Select an option below.")
printslow.slow_type("1. Order")
printslow.slow_type("2. Checkout")
printslow.slow_type("3. Inventory")
printslow.slow_type("4. Exit")

while True:
    selection = input(">> ")
    if selection == "1":
        order.start()
    elif selection == "2":
        Checkout.start()
    elif selection == "3":
        inventory.start()
    elif selection == "4":
        printslow.slow_type("Fine, didn't want you here anyway!")
        break
    else:
        printslow.slow_type("Stop being a failure. It is 1, 2, or 3. Not that difficult.")