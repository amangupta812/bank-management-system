import tkinter as tk
from tkinter import messagebox

from transactions.transaction import withdraw


def show_withdrawal(parent):

    window = tk.Toplevel(parent)

    window.title("Withdraw Money")
    window.geometry("450x350")

    tk.Label(
        window,
        text="Withdraw Money",
        font=("Arial", 18, "bold")
    ).pack(pady=25)

    frame = tk.Frame(window)
    frame.pack()

    # Account number
    tk.Label(
        frame,
        text="Account Number:"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    account_entry = tk.Entry(
        frame,
        width=25
    )

    account_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    # Amount
    tk.Label(
        frame,
        text="Amount:"
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    amount_entry = tk.Entry(
        frame,
        width=25
    )

    amount_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    def submit():

        account_number = account_entry.get().strip()
        amount = amount_entry.get().strip()

        if not account_number or not amount:
            messagebox.showerror(
                "Error",
                "Please fill in all fields."
            )
            return

        try:
            account_number = int(account_number)
            amount = float(amount)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Enter valid numbers."
            )
            return

        success, result = withdraw(
            account_number,
            amount
        )

        if success:

            messagebox.showinfo(
                "Withdrawal Successful",
                f"Withdrawal successful!\n\n"
                f"Amount: ₹{amount:.2f}\n"
                f"Remaining Balance: ₹{result:.2f}"
            )

            account_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)

        else:

            messagebox.showerror(
                "Withdrawal Failed",
                result
            )

    tk.Button(
        window,
        text="Withdraw",
        command=submit,
        width=20,
        font=("Arial", 12)
    ).pack(pady=30)