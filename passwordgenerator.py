import tkinter as tk
import random
import string

def generate_password():
    length = int(length_var.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Styling
root.configure(bg="#f0f0f0")
title_font = ("Helvetica", 20, "bold")
button_font = ("Helvetica", 14)
label_font = ("Helvetica", 12)

main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(padx=20, pady=20)

title_label = tk.Label(main_frame, text="Password Generator", font=title_font, bg="#f0f0f0")
title_label.pack(pady=(0, 10))

length_label = tk.Label(main_frame, text="Password Length:", font=label_font, bg="#f0f0f0")
length_label.pack()

length_var = tk.StringVar()
length_entry = tk.Entry(main_frame, textvariable=length_var, font=label_font)
length_entry.pack(pady=5)

generate_button = tk.Button(main_frame, text="Generate Password", font=button_font, command=generate_password)
generate_button.pack(pady=10)

password_var = tk.StringVar()
password_label = tk.Label(main_frame, textvariable=password_var, font=label_font, bg="#f0f0f0")
password_label.pack()

root.mainloop()
