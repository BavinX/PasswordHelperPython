import tkinter as tk
from tkinter import messagebox
from passwordHelper import check_password_strength

def check_password():
    password = entry_password.get()
    if password:
        strength_result = check_password_strength(password)
        label_strength.config(text=strength_result)
    else:
        messagebox.showwarning("Warning", "Please enter a password.")

# Create the main window
window = tk.Tk()
window.title("Password Strength Checker")

# Create an Entry widget for password input
entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=10)

# Create a Button to check password strength
button_check = tk.Button(window, text="Check Strength", command=check_password)
button_check.pack(pady=5)

# Create a Label to display password strength
label_strength = tk.Label(window, text="", fg="blue")
label_strength.pack(pady=10)

# Run the main event loop
window.mainloop()
