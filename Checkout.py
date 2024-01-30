import printslow
def start(order):
    subtotal = 0
    tax_rate = 0.095
    print("Customer Order:")
    for i in order:
        print(i.quantity, i.size, i.type, i.price)
        subtotal += i.quantity * i.price
    subtotal = round(subtotal, 2)
    tax = round(subtotal * tax_rate, 2)
    total = round(tax + subtotal, 2)
    print("Subtotal: $" + str(subtotal))
    print("Tax: $" + str(tax))
    print("Total: $" + str(total))
    payment(total)
    input("(Press ENTER you pizza loving swine!)")

def payment(total):
    while True:
        printslow.slow_type("Cash or credit?")
        payment_type = input(">> ")
        if payment_type.lower() == "cash":
            printslow.slow_type(f"The total is ${total}.")
            cash = int(input("Enter cash eceived: "))
            change = round(cash - total, 2)
            printslow.slow_type(f"Return ${change} to the customer.")
            input("(Press ENTER you pizza loving swine!)")
            break
        elif payment_type.lower() == "credit":
            printslow.slow_type(f"The toal is ${total}")
            printslow.slow_type("Please swipe the credit card")
            input("(Press ENTER you pizza loving swine!)")
            break
        else:
            printslow.slow_type("Cash or credit idiot put the right thing. I stg I will steal all of your money!")
            input("(Press ENTER you pizza loving swine! )")