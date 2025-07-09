import tkinter as tk
from tkinter import ttk, messagebox

from validators.email_dfa import is_valid_email
from validators.phone_dfa import is_valid_phone

from validators.date_dfa import is_valid_date

def validate_input():
    data = entry.get()
    choice = combo.get()

    if choice == "Email":
        valid = is_valid_email(data)
    elif choice == "Phone":
        valid = is_valid_phone(data)
 
    elif choice == "Date":
        valid = is_valid_date(data)
    else:
        valid = False

    msg = "VALID ✅" if valid else "INVALID ❌"
    messagebox.showinfo("Validation Result", f"{choice} is {msg}")

# GUI Setup
root = tk.Tk()
root.title("TOC-Based Regex Input Validator")
root.geometry("400x200")

tk.Label(root, text="Select Input Type:").pack(pady=5)
combo = ttk.Combobox(root, values=["Email", "Phone", "Date"], state="readonly")
combo.pack()

tk.Label(root, text="Enter Input:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack()

tk.Button(root, text="Validate", command=validate_input, bg="lightblue").pack(pady=20)

root.mainloop()
