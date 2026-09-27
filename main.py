import tkinter as tk

from database.db import create_database

from gui.customer_gui import show_customer_registration
from gui.account_gui import show_account_creation
from gui.deposit_gui import show_deposit
from gui.withdrawal_gui import show_withdrawal
from gui.balance_gui import show_balance
from gui.transfer_gui import show_transfer
from gui.transaction_gui import show_transaction_history

def main():

    create_database()

    window = tk.Tk()

    window.title("Bank Management System")
    window.geometry("500x550")

    tk.Label(
        window,
        text="Bank Management System",
        font=("Arial", 20, "bold")
    ).pack(pady=30)

    # Customer registration
    tk.Button(
        window,
        text="Register Customer",
        width=25,
        command=lambda:
            show_customer_registration(window)
    ).pack(pady=8)

    # Account creation
    tk.Button(
        window,
        text="Create Bank Account",
        width=25,
        command=lambda:
            show_account_creation(window)
    ).pack(pady=8)

    # Deposit
    tk.Button(
        window,
        text="Deposit Money",
        width=25,
        command=lambda:
            show_deposit(window)
    ).pack(pady=8)

    # Withdrawal
    tk.Button(
        window,
        text="Withdraw Money",
        width=25,
        command=lambda:
            show_withdrawal(window)
    ).pack(pady=8)

    # Balance
    tk.Button(
        window,
        text="Check Balance",
        width=25,
        command=lambda:
            show_balance(window)
    ).pack(pady=8)

    #Transfer
    tk.Button(
        window,
        text="Transfer Money",
        width=25,
        command=lambda:
            show_transfer(window)
    ).pack(pady=8)
    
    #Transaction history
    tk.Button(
        window,
        text="Transaction History",
        width=25,
        command=lambda:
            show_transaction_history(window)
    ).pack(pady=8)

    window.mainloop()


if __name__ == "__main__":
    main()