import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("300x300+750+250")

        self.label_strength = tk.Label(root, text="Password Strength:")
        self.label_strength.pack()

        self.strength_var = tk.StringVar()
        self.strength_var.set("medium")

        self.radio_strong = tk.Radiobutton(root, text="Strong", variable=self.strength_var, value="strong")
        self.radio_strong.pack()

        self.radio_medium = tk.Radiobutton(root, text="Medium", variable=self.strength_var, value="medium")
        self.radio_medium.pack()

        self.radio_easy = tk.Radiobutton(root, text="Easy", variable=self.strength_var, value="easy")
        self.radio_easy.pack()

        self.label_length = tk.Label(root, text="Password Length:")
        self.label_length.pack()

        self.password_length = tk.Entry(root)
        self.password_length.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.generated_password = tk.Label(root, text="")
        self.generated_password.pack()

    def generate_password(self):
        strength = self.strength_var.get()
        length = int(self.password_length.get())

        if strength == "strong":
            characters = string.ascii_letters + string.digits + string.punctuation
        elif strength == "medium":
            characters = string.ascii_letters + string.digits
        else:
            characters = string.ascii_lowercase

        password = ''.join(random.choice(characters) for _ in range(length))
        

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
