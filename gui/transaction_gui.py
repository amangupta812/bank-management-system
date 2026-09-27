import tkinter as tk
from tkinter import messagebox, ttk

from transactions.transaction import get_transaction_history


def show_transaction_history(parent):

    window = tk.Toplevel(parent)

    window.title("Transaction History")
    window.geometry("850x500")

    tk.Label(
        window,
        text="Transaction History",
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    # Search section
    search_frame = tk.Frame(window)
    search_frame.pack(pady=5)

    tk.Label(
        search_frame,
        text="Account Number:"
    ).grid(
        row=0,
        column=0,
        padx=10
    )

    account_entry = tk.Entry(
        search_frame,
        width=25
    )

    account_entry.grid(
        row=0,
        column=1,
        padx=10
    )

    # Table
    columns = (
        "ID",
        "Type",
        "Amount",
        "Date",
        "Description"
    )

    table = ttk.Treeview(
        window,
        columns=columns,
        show="headings",
        height=15
    )

    # Column headings
    table.heading(
        "ID",
        text="ID"
    )

    table.heading(
        "Type",
        text="Type"
    )

    table.heading(
        "Amount",
        text="Amount"
    )

    table.heading(
        "Date",
        text="Date"
    )

    table.heading(
        "Description",
        text="Description"
    )

    # Column widths
    table.column(
        "ID",
        width=50
    )

    table.column(
        "Type",
        width=100
    )

    table.column(
        "Amount",
        width=100
    )

    table.column(
        "Date",
        width=160
    )

    table.column(
        "Description",
        width=300
    )

    table.pack(
        padx=20,
        pady=20,
        fill="both",
        expand=True
    )

    def search_transactions():

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

        success, result = get_transaction_history(
            account_number
        )

        if not success:

            messagebox.showerror(
                "Error",
                result
            )

            return

        # Clear existing rows
        for row in table.get_children():

            table.delete(row)

        # Insert transactions
        for transaction in result:

            transaction_id = transaction[0]
            transaction_type = transaction[1]
            amount = transaction[2]
            transaction_date = transaction[3]
            description = transaction[4]

            table.insert(
                "",
                tk.END,
                values=(
                    transaction_id,
                    transaction_type,
                    f"₹{amount:.2f}",
                    transaction_date,
                    description
                )
            )

        if not result:

            messagebox.showinfo(
                "Transaction History",
                "No transactions found for this account."
            )

    tk.Button(
        search_frame,
        text="View History",
        command=search_transactions,
        width=15
    ).grid(
        row=0,
        column=2,
        padx=10
    )