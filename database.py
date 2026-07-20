import sqlite3


# Database Connection
def connect_db():
    return sqlite3.connect("expense.db")


# Create Tables
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Salary(
        SalaryID INTEGER PRIMARY KEY AUTOINCREMENT,
        Month TEXT,
        SalaryAmount REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Expense(
        ExpenseID INTEGER PRIMARY KEY AUTOINCREMENT,
        Date TEXT,
        Category TEXT,
        Amount REAL,
        Description TEXT
    )
    """)

    conn.commit()
    conn.close()


# Save Salary
def save_salary(month, salary):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Salary (Month, SalaryAmount) VALUES (?, ?)",
        (month, salary)
    )

    conn.commit()
    conn.close()


# Get Latest Salary
def get_latest_salary():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SalaryAmount
        FROM Salary
        ORDER BY SalaryID DESC
        LIMIT 1
    """)

    data = cursor.fetchone()

    conn.close()

    if data:
        return data[0]
    return 0


# Save Expense
def save_expense(date, category, amount, description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Expense(Date, Category, Amount, Description)
        VALUES (?, ?, ?, ?)
    """, (date, category, amount, description))

    conn.commit()
    conn.close()


# Get Total Expenses
def get_total_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
SELECT SUM(Amount)
FROM Expense
WHERE strftime('%Y-%m', Date) = strftime('%Y-%m', 'now')
""")

    total = cursor.fetchone()[0]

    conn.close()

    if total is None:
        return 0

    return total

def get_category_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
SELECT Category, SUM(Amount)
FROM Expense
WHERE strftime('%Y-%m', Date) = strftime('%Y-%m', 'now')
GROUP BY Category
""")

    data = cursor.fetchall()

    conn.close()

    return data
def get_all_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ExpenseID, Date, Category, Amount, Description
        FROM Expense
        ORDER BY ExpenseID DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data
# Create tables automatically
create_tables()


if __name__ == "__main__":
    create_tables()
    print("Database created successfully!")
if __name__ == "__main__":
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT Category, Amount FROM Expense")
    print(cursor.fetchall())

    conn.close()