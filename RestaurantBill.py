order1 = "Hamburger"
order1Quantity = 4
order1price = 7

order2 = "Fruit Salad"
order2Quantity = 3
order2price = 10

order3 = "Soda"
order3Quantity = 2
order3price = 5

order1cost = order1Quantity * order1price
order2cost = order2Quantity * order2price
order3cost = order3Quantity * order3price

total = order1cost + order2cost + order3cost
tax = total * 0.20
total_cost = total + tax


#Finall Bill
print("WELCOME To HAMZA's\nRESTAURANT")
print(f"\n1: {order1} = {order1Quantity} x {order1price} = {order1cost}$")
print(f"2: {order2} = {order2Quantity} x {order2price} = {order2cost}$")
print(f"3: {order3} = {order3Quantity} x {order3price} = {order3cost}$")
print("\n-----------------------")
print(f"Total = {total}$")
print(f"Tax = {tax}$")
print("------------------------")
print(f"\nTotal Cost = {total_cost}$")
print("\nThank you")
