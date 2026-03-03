# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish.\n")

while True:
    stock = input("Enter stock name: ").upper()
    
    if stock == "DONE":
        break
    
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    else:
        print(" Stock not available. Please choose from the list.")

print("\n Portfolio Summary:")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock} - {quantity} shares ${price} = ${investment}")

print(f"\n Total Investment Value: ${total_investment}")

# Optional: Save to file
save_option = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save_option == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock} - {quantity} shares ${price} = ${investment}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")
    
    print(" Portfolio saved as portfolio_summary.txt")

print("\nThank you for using Stock Portfolio Tracker!")