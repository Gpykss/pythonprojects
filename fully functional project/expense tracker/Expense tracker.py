import csv
from datetime import datetime
from pathlib import Path

CSV_FILE = Path("expenses.csv")
CSV_HEADERS = ["date", "category", "description", "amount"]

def ensure_csv():
    """Create file with headers if missing."""
    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)

def add_expense():
    """Add a new expense."""
    date = input("Enter date (YYYY-MM-DD, leave empty for today): ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter category (e.g. food, transport): ").strip()
    description = input("Enter description: ").strip()
    amount = input("Enter amount: ").strip()

    ensure_csv()
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, description, amount])

    print("✅ Expense added!")

def view_expenses():
    """View all expenses in a table."""
    ensure_csv()
    with CSV_FILE.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("No expenses found.")
        return

    print("\n📒 Expenses:")
    print("-" * 60)
    print(f"{'Date':<12} {'Category':<15} {'Amount':>10}  Description")
    print("-" * 60)

    total = 0
    for row in rows:
        print(f"{row['date']:<12} {row['category']:<15} {row['amount']:>10}  {row['description']}")
        try:
            total += float(row["amount"])
        except ValueError:
            pass

    print("-" * 60)
    print(f"{'Total':<28} {total:>10.2f}\n")

def menu():
    """Simple text menu."""
    while True:
        print("==== Expense Tracker ====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
