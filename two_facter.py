import tkinter as tk
from tkinter import messagebox
import random

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("800x400")

        self.username = "user"
        self.password = "pwd123"
        self.two_factor_code = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Username:").pack(pady=5)
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack(pady=5)

        tk.Label(self.root, text="Password:").pack(pady=5)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.authenticate).pack(pady=20)

    def generate_2fa_code(self):
        self.two_factor_code = random.randint(100000, 999999)
        print(f"Your 2FA code is: {self.two_factor_code}")

    def authenticate(self):
        entered_username = self.entry_username.get()
        entered_password = self.entry_password.get()

        if entered_username == self.username and entered_password == self.password:
            self.generate_2fa_code()
            self.open_2fa_window()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def open_2fa_window(self):
        self.two_fa_window = tk.Toplevel(self.root)
        self.two_fa_window.title("2FA Verification")
        self.two_fa_window.geometry("300x150")

        tk.Label(self.two_fa_window, text="Enter 2FA Code:").pack(pady=10)
        self.entry_2fa = tk.Entry(self.two_fa_window)
        self.entry_2fa.pack(pady=5)

        tk.Button(self.two_fa_window, text="Verify", command=self.verify_2fa).pack(pady=10)

    def verify_2fa(self):
        entered_code = self.entry_2fa.get()

        if entered_code == str(self.two_factor_code):
            messagebox.showinfo("Success", "Login Successful!")
            self.two_fa_window.destroy()
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Invalid 2FA Code")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
