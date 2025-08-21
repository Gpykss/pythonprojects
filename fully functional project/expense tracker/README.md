
```markdown
# 🧾 Expense Tracker (Beginner Project)

A simple command-line **Expense Tracker** built with Python.  
This project allows users to **add expenses** (date, category, amount, description) and **view all expenses** in a clean tabular format.  
Data is stored in a CSV file for persistence.

---

## ✨ Features
- Add new expenses
- View all expenses neatly formatted
- Data saved in `expenses.csv` for later use
- Beginner-friendly code (no external libraries required)

---

## 🛠️ Tech Stack
- **Python 3**
- **CSV module**
- **pathlib (for file handling)**

---

## 📂 Project Structure
```

expense\_tracker/
│── expenses.csv   # CSV file (auto-created if not found)
│── tracker.py     # Main Python script
│── README.md      # Project documentation

````

---

## 🚀 How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
````

2. Navigate into the project folder:

   ```bash
   cd expense-tracker
   ```
3. Run the script:

   ```bash
   python tracker.py
   ```

---

## 📸 Example Usage

```
1. Add expense
2. View expenses
3. Quit
Choose: 1
Enter date (YYYY-MM-DD): 2025-08-21
Enter category: Food
Enter amount: 12.50
Enter description: Lunch

Expense added!

1. Add expense
2. View expenses
3. Quit
Choose: 2

Date         Category            Amount  Description
----------------------------------------------------
2025-08-21   Food                   12.50  Lunch
```

---

## 📌 Notes

* This is a **beginner-level project** (no Pandas/Numpy required).
* Useful for practicing file handling, CSV, and string formatting in Python.

---

## 👤 Author

**Gpyks**

* GitHub: [Gpykss](https://github.com/Gpykss)

