import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
    
    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol}")
    
    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if self.portfolio[symbol] > shares:
                self.portfolio[symbol] -= shares
                print(f"Removed {shares} shares of {symbol}")
            else:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol}")
        else:
            print(f"Stock {symbol} not found in portfolio")
    
    def view_portfolio(self):
        if not self.portfolio:
            print("Portfolio is empty")
            return
        print("Current Portfolio:")
        for symbol, shares in self.portfolio.items():
            stock = yf.Ticker(symbol)
            price = stock.history(period="1d").iloc[-1]['Close']
            value = price * shares
            print(f"{symbol}: {shares} shares, Price: ${price:.2f}, Value: ${value:.2f}")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. View Portfolio\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == "2":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == "3":
            portfolio.view_portfolio()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")
