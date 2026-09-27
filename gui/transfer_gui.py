import tkinter as tk
from tkinter import messagebox

from transactions.transaction import transfer


def show_transfer(parent):

    window = tk.Toplevel(parent)

    window.title("Transfer Money")
    window.geometry("500x400")

    tk.Label(
        window,
        text="Transfer Money",
        font=("Arial", 18, "bold")
    ).pack(pady=25)

    frame = tk.Frame(window)
    frame.pack()

    # Source account
    tk.Label(
        frame,
        text="From Account:"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    source_entry = tk.Entry(
        frame,
        width=25
    )

    source_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    # Destination account
    tk.Label(
        frame,
        text="To Account:"
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    destination_entry = tk.Entry(
        frame,
        width=25
    )

    destination_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    # Amount
    tk.Label(
        frame,
        text="Amount:"
    ).grid(
        row=2,
        column=0,
        padx=10,
        pady=10
    )

    amount_entry = tk.Entry(
        frame,
        width=25
    )

    amount_entry.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )

    def submit():

        source = source_entry.get().strip()
        destination = destination_entry.get().strip()
        amount = amount_entry.get().strip()

        if not source or not destination or not amount:
            messagebox.showerror(
                "Error",
                "Please fill in all fields."
            )
            return

        try:
            source = int(source)
            destination = int(destination)
            amount = float(amount)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Enter valid numbers."
            )
            return

        success, result = transfer(
            source,
            destination,
            amount
        )

        if success:

            source_balance, destination_balance = result

            messagebox.showinfo(
                "Transfer Successful",
                f"Transfer successful!\n\n"
                f"Amount: ₹{amount:.2f}\n\n"
                f"From Account: {source}\n"
                f"New Balance: ₹{source_balance:.2f}\n\n"
                f"To Account: {destination}\n"
                f"New Balance: ₹{destination_balance:.2f}"
            )

            source_entry.delete(0, tk.END)
            destination_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)

        else:

            messagebox.showerror(
                "Transfer Failed",
                result
            )

    tk.Button(
        window,
        text="Transfer Money",
        command=submit,
        width=20,
        font=("Arial", 12)
    ).pack(pady=30)