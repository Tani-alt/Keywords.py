menu = {
    "Burger": 5.50,
    "Pizza": 8.00,
    "Pasta": 7.50,
    "Salad": 4.00,
    "Soda": 1.50
}

def calculate_bill():
    total = 0
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price} ")
    item1 = input("\nEnter first item you want to order: ").capitalize()
    if item1 in menu:
        quantity1 = int(input(f"How many {item1}s would you like? "))
        total += menu[item1] * quantity1
    else:
        print("Item not on the menu.")

    item2 = input("Enter second item you want to order: ").capitalize()
    if item2 in menu:
        quantity2 = int(input(f"How many {item2}s would you like? "))
        total += menu[item2] * quantity2
    else:
        print("Item not on the menu.")
    
    item3 = input("Enter third item you want to order: ").capitalize()
    if item3 in menu:
        quantity3 = int(input(f"How many {item3}s would you like? "))
        total += menu[item3] * quantity3
    else:
        print("Item not on the menu.")

    return total

def main():
    total = calculate_bill()
    print(f"\nTotal amount: ${total:.2f}")
    
    tip_percentage = float(input("Enter tip percentage (e.g., 15 for 15%): "))
    tip = total * (tip_percentage / 100)
    final_total = total + tip
    
    print(f"Tip: ${tip:.2f}")
    print(f"Final total: ${final_total:.2f}")
    print("CASH OR CARD OR UPI")

if __name__ == "__main__":
    main()