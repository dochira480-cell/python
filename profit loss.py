actual_cost = float(input("Enter the actual cost of the item: "))
sale_price = float(input("Enter the selling price of the item: "))
profit_loss = sale_price - actual_cost
if profit_loss > 0:
    print(f"You made a profit of: ${profit_loss:.2f}")
elif profit_loss < 0:
    print(f"You incurred a loss of: ${-profit_loss:.2f}")
else:
    print("No profit, no loss.")