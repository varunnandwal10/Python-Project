import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ''
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "Please select at least one character type."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for length.")

# Create GUI window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase", variable=lower_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w', padx=20)

tk.Button(root, text="Generate Password", command=on_generate).pack(pady=10)

result_label = tk.Label(root, text="Generated Password: ")
result_label.pack(pady=10)

# Run the app
root.mainloop()
