age = int(input("Input age: ")) # Do not change this line
ticket = float(30.0)
if age >= 65:
    ticket_price = ticket / 2
    print(ticket_price)
elif age <= 5:
    print(0.0)

else:
    print(ticket)    