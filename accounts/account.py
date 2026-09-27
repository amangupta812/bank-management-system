from datetime import datetime
from database.db import get_connection


def create_account(customer_id, account_type, initial_deposit):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Check if customer exists
        cursor.execute(
            "SELECT customer_id FROM customers WHERE customer_id = ?",
            (customer_id,)
        )

        customer = cursor.fetchone()

        if customer is None:
            return False, "Customer ID does not exist."

        # Make sure deposit is valid
        if initial_deposit < 0:
            return False, "Initial deposit cannot be negative."

        # Generate account number
        cursor.execute(
            "SELECT MAX(account_number) FROM accounts"
        )

        last_account = cursor.fetchone()[0]

        if last_account is None:
            account_number = 100001
        else:
            account_number = last_account + 1

        # Current date
        created_date = datetime.now().strftime("%Y-%m-%d")

        # Insert account
        cursor.execute("""
            INSERT INTO accounts
            (
                account_number,
                customer_id,
                account_type,
                balance,
                created_date
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            account_number,
            customer_id,
            account_type,
            initial_deposit,
            created_date
        ))
        
        # Record initial deposit as a transaction
        cursor.execute("""
            INSERT INTO transactions
            (
                account_number,
                transaction_type,
                amount,
                transaction_date,
                description
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            account_number,
            "Deposit",
            initial_deposit,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Initial account deposit"
        ))

        connection.commit()

        return True, account_number

    except Exception as error:
        connection.rollback()
        return False, str(error)

    finally:
        connection.close()