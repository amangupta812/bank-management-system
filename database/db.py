import sqlite3

DATABASE_NAME = "bank.db"

def get_connection():
    return sqlite3.connect(DATABASE_NAME)


    # Enable foreign key support
    connection.execute("PRAGMA foreign_keys = ON")

    return connection

# ---------------- DATABASE ----------------

def create_database():
    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            address TEXT NOT NULL,
            date_of_birth TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_number INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            account_type TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0,
            created_date TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    """)

    # Transactions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number INTEGER NOT NULL,
            transaction_type TEXT NOT NULL,
            amount REAL NOT NULL,
            transaction_date TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (account_number)
                REFERENCES accounts(account_number)
        )
""")


    connection.commit()
    connection.close()