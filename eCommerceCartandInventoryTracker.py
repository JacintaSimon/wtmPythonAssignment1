#Available Inventory: Item Name -> Unit Price
catalog = {"laptop":800, "mouse":20, "keyboard":50, "monitor":150}

grand_total = 0.0

while True:
    item = input("Enter item to buy (or 'checkout' / 'exit'): ").lower().strip()

    if item == "exit":
        break

    elif item == "checkout":
        if grand_total >= 500:
            rate = 0.10
        elif grand_total >= 200:
            rate = 0.05
        else:
            rate = 0.0 

        discount = round(grand_total * rate, 2)
        final_total = round(grand_total - discount, 2)

        print("\nCHECKOUT RECEIPT")
        print("=" * 40)
        print(f"Subtotal: ${grand_total}")
        print(f"Discount: ${discount}")
        print(f"Final Total: ${final_total}")
        print("=" * 40)
        break

    elif item in catalog:
        price = catalog[item]
        grand_total += price
        print(f"-->Added {item.capitalize()} (${price}) to order.")

    else:
        print("-->[ERROR] Item not found in catalog. Try again.")
