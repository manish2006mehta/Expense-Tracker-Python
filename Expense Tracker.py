#Expense Tracker Project
print("Welcome to Expense Tracker\n")
expenses = []
while(True):
    print("========== MENU ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. Exit")
    print("==========================")
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a number only.")
        continue

    if choice == 1:
        date = input("Enter date (DD-MM-YYYY): ")
        product = input("Enter product name: ")
        category = input("Enter product category: ")
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Amount must be a number.")
            continue

        expense = {
            "Date": date, 
            "Product": product, 
            "Category": category, 
            "Amount": amount
            }
        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == 2:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\n--- Expense List ---")
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp['Date']} | {exp['Product']} | {exp['Category']} | ₹{exp['Amount']}")

    elif choice == 3:
        if not expenses:
            print("No expenses to calculate.")
        else:
            spend = 0
            for kharcha in expenses:
                spend += kharcha["Amount"]
        print(f"Total spending amount is ₹{spend}.")    
    elif choice == 4:
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Enter a valid choice (1-4): ")
