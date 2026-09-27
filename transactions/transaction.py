from datetime import datetime
from database.db import get_connection


def deposit(account_number, amount):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Check amount
        if amount <= 0:
            return False, "Deposit amount must be greater than zero."

        # Check account
        cursor.execute("""
            SELECT balance
            FROM accounts
            WHERE account_number = ?
        """, (account_number,))

        account = cursor.fetchone()

        if account is None:
            return False, "Account number does not exist."

        # Update balance
        new_balance = account[0] + amount

        cursor.execute("""
            UPDATE accounts
            SET balance = ?
            WHERE account_number = ?
        """, (new_balance, account_number))

        # Record transaction
        transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
            amount,
            transaction_date,
            "Cash deposit"
        ))

        connection.commit()

        return True, new_balance

    except Exception as error:
        connection.rollback()
        return False, str(error)

    finally:
        connection.close()

# ---------------- Add withdrawal ----------------

def withdraw(account_number, amount):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Check amount
        if amount <= 0:
            return False, "Withdrawal amount must be greater than zero."

        # Get current balance
        cursor.execute("""
            SELECT balance
            FROM accounts
            WHERE account_number = ?
        """, (account_number,))

        account = cursor.fetchone()

        if account is None:
            return False, "Account number does not exist."

        current_balance = account[0]

        # Check sufficient balance
        if amount > current_balance:
            return False, "Insufficient balance."

        # Calculate new balance
        new_balance = current_balance - amount

        # Update account
        cursor.execute("""
            UPDATE accounts
            SET balance = ?
            WHERE account_number = ?
        """, (new_balance, account_number))

        # Record transaction
        transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
            "Withdrawal",
            amount,
            transaction_date,
            "Cash withdrawal"
        ))

        connection.commit()

        return True, new_balance

    except Exception as error:
        connection.rollback()
        return False, str(error)

    finally:
        connection.close()

# ---------------- Add balance checking ----------------

def get_balance(account_number):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT balance
            FROM accounts
            WHERE account_number = ?
        """, (account_number,))

        account = cursor.fetchone()

        if account is None:
            return False, "Account number does not exist."

        return True, account[0]

    except Exception as error:
        return False, str(error)

    finally:
        connection.close()

# ---------------- account-to-account transfer ----------------

def transfer(source_account, destination_account, amount):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Validate amount
        if amount <= 0:
            return False, "Transfer amount must be greater than zero."

        # Prevent transferring to the same account
        if source_account == destination_account:
            return False, "Source and destination accounts cannot be the same."

        # Get source account
        cursor.execute("""
            SELECT balance
            FROM accounts
            WHERE account_number = ?
        """, (source_account,))

        source = cursor.fetchone()

        if source is None:
            return False, "Source account does not exist."

        # Get destination account
        cursor.execute("""
            SELECT balance
            FROM accounts
            WHERE account_number = ?
        """, (destination_account,))

        destination = cursor.fetchone()

        if destination is None:
            return False, "Destination account does not exist."

        # Check balance
        source_balance = source[0]

        if amount > source_balance:
            return False, "Insufficient balance."

        # Calculate new balances
        new_source_balance = source_balance - amount
        new_destination_balance = destination[0] + amount

        # Update source account
        cursor.execute("""
            UPDATE accounts
            SET balance = ?
            WHERE account_number = ?
        """, (
            new_source_balance,
            source_account
        ))

        # Update destination account
        cursor.execute("""
            UPDATE accounts
            SET balance = ?
            WHERE account_number = ?
        """, (
            new_destination_balance,
            destination_account
        ))

        transaction_date = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Record outgoing transaction
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
            source_account,
            "Transfer",
            amount,
            transaction_date,
            f"Transfer to account {destination_account}"
        ))

        # Record incoming transaction
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
            destination_account,
            "Transfer",
            amount,
            transaction_date,
            f"Transfer from account {source_account}"
        ))

        connection.commit()

        return True, (
            new_source_balance,
            new_destination_balance
        )

    except Exception as error:
        connection.rollback()
        return False, str(error)

    finally:
        connection.close()

# ---------------- Transaction-history ----------------

def get_transaction_history(account_number):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Check if account exists
        cursor.execute("""
            SELECT account_number
            FROM accounts
            WHERE account_number = ?
        """, (account_number,))

        account = cursor.fetchone()

        if account is None:
            return False, "Account number does not exist."

        # Get transactions
        cursor.execute("""
            SELECT
                transaction_id,
                transaction_type,
                amount,
                transaction_date,
                description
            FROM transactions
            WHERE account_number = ?
            ORDER BY transaction_id DESC
        """, (account_number,))

        transactions = cursor.fetchall()

        return True, transactions

    except Exception as error:

        return False, str(error)

    finally:

        connection.close()        