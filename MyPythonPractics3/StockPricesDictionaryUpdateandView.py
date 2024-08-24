stock_prices = {}

def update_stock(symbol, price):
    stock_prices[symbol] = price

def view_stocks():
    for symbol, price in stock_prices.items():
        print(f"{symbol}: ${price}")

while True:
    command = input("Enter a command (update, view, exit): ").strip().lower()
    if command == 'update':
        symbol = input("Enter stock symbol: ")
        price = float(input("Enter stock price: "))
        update_stock(symbol, price)
    elif command == 'view':
        view_stocks()
    elif command == 'exit':
        break
    else:
        print("Unknown command")


# Stock Prices Dictionary Update and View