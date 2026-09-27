import tkinter as tk
from tkinter import messagebox

from transactions.transaction import get_balance


def show_balance(parent):

    window = tk.Toplevel(parent)

    window.title("Check Balance")
    window.geometry("450x300")

    tk.Label(
        window,
        text="Check Account Balance",
        font=("Arial", 18, "bold")
    ).pack(pady=25)

    frame = tk.Frame(window)
    frame.pack()

    tk.Label(
        frame,
        text="Account Number:"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=15
    )

    account_entry = tk.Entry(
        frame,
        width=25
    )

    account_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=15
    )

    def check():

        account_number = account_entry.get().strip()

        if not account_number:
            messagebox.showerror(
                "Error",
                "Enter an account number."
            )
            return

        try:
            account_number = int(account_number)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Account number must be a number."
            )
            return

        success, result = get_balance(
            account_number
        )

        if success:

            messagebox.showinfo(
                "Account Balance",
                f"Account Number: {account_number}\n\n"
                f"Current Balance: ₹{result:.2f}"
            )

        else:

            messagebox.showerror(
                "Error",
                result
            )

    tk.Button(
        window,
        text="Check Balance",
        command=check,
        width=20,
        font=("Arial", 12)
    ).pack(pady=25)