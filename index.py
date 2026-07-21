# Simple Expense Tracker
# Author: Md Shakil Khan
# Description: A beginner-friendly Python project to track daily expenses

expenses = []


def add_expense():
    """Add a new expense."""
    name = input("Enter expense name: ")
    
    try:
        amount = float(input("Enter expense amount: $"))
        expenses.append({"name": name, "amount": amount})
        print("Expense added successfully!\n")

    except ValueError:
        print("Please enter a valid amount.\n")


def show_expenses():
    """Display all expenses."""
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\n--- Expense List ---")

    total = 0

    for expense in expenses:
        print(f"{expense['name']}: ${expense['amount']:.2f}")
        total += expense["amount"]

    print("--------------------")
    print(f"Total Expense: ${total:.2f}\n")


def main():
    """Main program menu."""

    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()