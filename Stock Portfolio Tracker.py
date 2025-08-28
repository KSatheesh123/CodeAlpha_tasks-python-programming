stock_prices={"AAPL": 180,"TSLA": 250,"GOOG":3100,"MSFT":350}
print("------Stock Portfolio Tracker------\n")
print("Stock available:",','.join(stock_prices.keys()));
portfolio={}
investment1={}
total=0
while True:
    stock=input("Enter a stock (or type 'OVER' to finish):").upper();
    if stock in stock_prices:
        qty=int(input("Entter the quantity:"))
        portfolio[stock]=qty
        investment=qty*stock_prices[stock]
        investment1[stock]=investment;
    elif (stock=="OVER"):
        break;
    else:
        print("Given stock is not available")
        continue
    total=total+investment
print("\nPortfolio Summary!!\n")
for stock, qty in portfolio.items():
    print(f"{stock} -> {qty} shares × ${stock_prices[stock]} = $",investment1[stock])
print("Total investment:$",total);
save_choice = input("\nDo you want to save results to a file? (yes/no): ").lower()
if save_choice == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock} -> {qty} shares × ${stock_prices[stock]} = ${investment1[stock]}")
        f.write(f"Total investment:${total}")
    print("\nPortfolio saved to portfolio.txt!!!")
