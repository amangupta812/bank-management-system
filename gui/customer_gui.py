import tkinter as tk
from tkinter import messagebox

from customers.customer import register_customer


def show_customer_registration(parent):

    window = tk.Toplevel(parent)

    window.title("Register Customer")
    window.geometry("450x400")

    tk.Label(
        window,
        text="Register Customer",
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    frame = tk.Frame(window)
    frame.pack()

    tk.Label(frame, text="Full Name:").grid(
        row=0, column=0, padx=10, pady=10
    )

    name_entry = tk.Entry(frame, width=30)
    name_entry.grid(
        row=0, column=1, padx=10, pady=10
    )

    tk.Label(frame, text="Phone:").grid(
        row=1, column=0, padx=10, pady=10
    )

    phone_entry = tk.Entry(frame, width=30)
    phone_entry.grid(
        row=1, column=1, padx=10, pady=10
    )

    tk.Label(frame, text="Address:").grid(
        row=2, column=0, padx=10, pady=10
    )

    address_entry = tk.Entry(frame, width=30)
    address_entry.grid(
        row=2, column=1, padx=10, pady=10
    )

    tk.Label(frame, text="Date of Birth:").grid(
        row=3, column=0, padx=10, pady=10
    )

    dob_entry = tk.Entry(frame, width=30)
    dob_entry.grid(
        row=3, column=1, padx=10, pady=10
    )

    def submit():

        success, message = register_customer(
            name_entry.get(),
            phone_entry.get(),
            address_entry.get(),
            dob_entry.get()
        )

        if success:
            messagebox.showinfo(
               "Customer Registered",
               f"Customer registered successfully!\n\n"
               f"Customer ID: {message}"
            )

            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
            dob_entry.delete(0, tk.END)

        else:
            messagebox.showerror("Error", message)

    tk.Button(
        window,
        text="Register Customer",
        command=submit,
        width=20
    ).pack(pady=25)