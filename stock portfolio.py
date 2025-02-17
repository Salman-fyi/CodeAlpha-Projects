portfolio = {}

while True:
    action = input("\n1) Add  2) Remove  3) Update  4) View  5) Exit\nChoose: ")

    if action == "1":
        s = input("Stock: ").upper()
        q = int(input("Quantity: "))
        p = float(input("Buy Price: "))
        c = float(input("Current Price: "))
        portfolio[s] = [q, p, c]

    elif action == "2":
        s = input("Stock to remove: ").upper()
        portfolio.pop(s, print("Stock not found."))

    elif action == "3":
        s = input("Stock to update: ").upper()
        if s in portfolio:
            portfolio[s][2] = float(input("New Price: "))
        else:
            print("Stock not found.")

    elif action == "4":
        for s, (q, p, c) in portfolio.items():
            print(f"{s}: {q} shares | Buy: ${p} | Now: ${c} | Change: {((c-p)/p)*100:.2f}%")

    elif action == "5":
        break

    else:
        print("Invalid choice.")
