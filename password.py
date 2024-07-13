import tkinter as tk
from tkinter import messagebox
import string
import secrets
def generate_password():
    length = length_var.get()  
    if length <= 0:
        messagebox.showerror("Error", "Password length should be greater than zero")
        return
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = lower + upper + digits + symbols
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    password_var.set(password)
root = tk.Tk()
root.title("PASSWORD GENERATER")
root.configure(bg="lightblue")
length_label = tk.Label(root, text="Password Length:", bg="lightblue", fg="white")
length_label.pack(pady=18)
length_var = tk.IntVar()
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="black", fg="white")
generate_button.pack(pady=18)
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("solid", 28), wraplength=500, bg="lightblue", fg="white")
password_label.pack(pady=18)
center_frame = tk.Frame(root, bg=" lightblue")
center_frame.pack(expand=True)
password_label.pack(in_=center_frame, pady=18)
root.mainloop()
