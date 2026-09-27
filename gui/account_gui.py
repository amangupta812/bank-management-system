import tkinter as tk
from tkinter import messagebox

from accounts.account import create_account


def show_account_creation(parent):

    window = tk.Toplevel(parent)

    window.title("Create Bank Account")
    window.geometry("450x400")

    # Title
    tk.Label(
        window,
        text="Create Bank Account",
        font=("Arial", 18, "bold")
    ).pack(pady=25)

    frame = tk.Frame(window)
    frame.pack()

    # Customer ID
    tk.Label(
        frame,
        text="Customer ID:"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
        sticky="w"
    )

    customer_id_entry = tk.Entry(
        frame,
        width=30
    )

    customer_id_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    # Account type
    tk.Label(
        frame,
        text="Account Type:"
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10,
        sticky="w"
    )

    account_type_var = tk.StringVar()
    account_type_var.set("Savings")

    account_type_menu = tk.OptionMenu(
        frame,
        account_type_var,
        "Savings",
        "Current"
    )

    account_type_menu.config(width=20)

    account_type_menu.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    # Initial deposit
    tk.Label(
        frame,
        text="Initial Deposit:"
    ).grid(
        row=2,
        column=0,
        padx=10,
        pady=10,
        sticky="w"
    )

    deposit_entry = tk.Entry(
        frame,
        width=30
    )

    deposit_entry.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )

    # Submit function
    def submit():

        customer_id = customer_id_entry.get().strip()
        account_type = account_type_var.get()
        deposit = deposit_entry.get().strip()

        # Empty field check
        if not customer_id or not deposit:
            messagebox.showerror(
                "Error",
                "Please fill in all fields."
            )
            return

        # Customer ID validation
        try:
            customer_id = int(customer_id)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Customer ID must be a number."
            )
            return

        # Deposit validation
        try:
            deposit = float(deposit)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Initial deposit must be a number."
            )
            return

        # Create account
        success, result = create_account(
            customer_id,
            account_type,
            deposit
        )

        if success:

            messagebox.showinfo(
                "Account Created",
                f"Account created successfully!\n\n"
                f"Account Number: {result}\n"
                f"Account Type: {account_type}\n"
                f"Initial Balance: ₹{deposit:.2f}"
            )

            customer_id_entry.delete(0, tk.END)
            deposit_entry.delete(0, tk.END)

        else:

            messagebox.showerror(
                "Error",
                result
            )

    # Button
    tk.Button(
        window,
        text="Create Account",
        command=submit,
        width=20,
        font=("Arial", 12)
    ).pack(pady=30)