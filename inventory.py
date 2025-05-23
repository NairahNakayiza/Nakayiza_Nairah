# Inventory Management System

# Lists to store item names and quantities
items = ["Pen", "Book", "Pencil"]
quantities = [10, 5, 20]

# Loop for menu
while True:
    print("\n--- Inventory Menu ---")
    print("1. Display Stock")
    print("2. Update Stock")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("\nCurrent Stock:")
        for i in range(len(items)):
            print(f"{items[i]}: {quantities[i]} units")

    elif choice == "2":
        item = input("Enter item name: ")
        qty = int(input("Enter new quantity: "))
        if item in items:
            index = items.index(item)
            quantities[index] = qty
            print(f"{item} updated to {qty} units.")
        else:
            items.append(item)
            quantities.append(qty)
            print(f"{item} added with {qty} units.")

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
