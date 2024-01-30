
import printslow, pandas, warnings
class Order:
    def __init__(self, quantity, size, type, price):
        self.quantity = quantity
        self.size = size
        self.type = type
        self.price = float(price[1:])
warnings.simplefilter(action='ignore', category=FutureWarning)
def start():
    order = []
    while True:
        printslow.slow_type("CHOOSE YOUR PIZZA!")
        pizza_menu = pandas.read_csv("data/types.csv")
        print(pizza_menu[["Type", "Size", "Price"]])
        printslow.slow_type("CHOOSE YOUR PIZZA!")
        selection = int(input(">> "))
        if selection > len(pizza_menu)-1:
            print("Hey, Stupid. Thats not a choice. be better.")
            continue 
        size = pizza_menu.iloc[selection][1]
        ptype = pizza_menu.iloc[selection][0]
        price = pizza_menu.iloc[selection][2]
        quantity = int(input(f"How Many {size} {ptype} pizzas do you think you will get? "))
        order.append(Order(quantity, size, ptype, price))
        printslow.slow_type("Sir/Mam would you like anotha? (y/n)")
        confirm = input (">> ")
        if confirm.lower() == "y":
            continue
        else:
            break
    for i in order:
        print(i.quantity, i.size, i.type, i.price)

    return order
    # with open("data/types.csv", newline = "") as csvfile:
    #     reader = csv.reader(csvfile)
    #     pizza_menu = list(reader)
    #     for pizza in pizza_menu:
    #         print(pizza[0], pizza[1], pizza[2])