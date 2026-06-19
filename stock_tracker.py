# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("=== Stock Portfolio Tracker ===")

n = int(input("How many stocks do you want to add? "))

for i in range(n):
    stock = input("Enter stock symbol: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available!")

print("\nPortfolio Summary")

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"{stock}: {quantity} shares = ${investment}")

print(f"\nTotal Investment Value = ${total_investment}")

with open("portfolio_summary.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("=================\n")

    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares = ${investment}\n")

    file.write(f"\nTotal Investment Value = ${total_investment}")

print("\nData saved to portfolio_summary.txt")