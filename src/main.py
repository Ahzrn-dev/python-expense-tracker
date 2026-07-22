from datetime import datetime

from database import Database


def print_menu() -> None:
    """Display the main menu."""

    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")


def add_expense(database: Database) -> None:
    """Add a new expense."""

    title = input("Title: ").strip()

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    category = input("Category: ").strip()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    database.add_expense(
        title,
        amount,
        category,
        created_at,
    )

    print("Expense added successfully.")


def view_expenses(database: Database) -> None:
    """Display all expenses."""

    expenses = database.get_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print()

    for expense in expenses:
        print(
            f"{expense[0]}. "
            f"{expense[1]} | "
            f"${expense[2]:.2f} | "
            f"{expense[3]} | "
            f"{expense[4]}"
        )


def delete_expense(database: Database) -> None:
    """Delete an expense."""

    try:
        expense_id = int(input("Expense ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    database.delete_expense(expense_id)

    print("Expense deleted successfully.")


def main() -> None:
    """Run the application."""

    database = Database()

    while True:
        print_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(database)

        elif choice == "2":
            view_expenses(database)

        elif choice == "3":
            delete_expense(database)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()