import customtkinter as ctk
import random
import string
import pyperclip

# --- 1. FUNCTIONS ---
def slider_event(value):
    length_label.configure(text=f"Length: {int(value)}")

def generate_password():
    char_pool = ""
    if low_var.get(): char_pool += string.ascii_lowercase
    if up_var.get():  char_pool += string.ascii_uppercase
    if num_var.get(): char_pool += string.digits
    if sym_var.get(): char_pool += string.punctuation

    if not char_pool:
        result_entry.delete(0, 'end')
        result_entry.insert(0, "Select character types!")
        return

    length = int(slider.get())
    password = "".join(random.choices(char_pool, k=length))
    result_entry.delete(0, 'end')
    result_entry.insert(0, password)
    copy_btn.configure(text="Copy", fg_color=("#3498db", "#1f6aa5")) # Reset copy button

def copy_to_clipboard():
    password = result_entry.get()
    if password and password != "Select character types!":
        pyperclip.copy(password)
        copy_btn.configure(text="Copied!", fg_color="green")
        app.after(1500, lambda: copy_btn.configure(text="Copy", fg_color=("#3498db", "#1f6aa5")))

# --- 2. SETUP APP ---
ctk.set_appearance_mode("dark")  # "dark", "light", "system"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("Password Generator")
app.geometry("600x400")

# Center the window
app.update_idletasks()
width = app.winfo_width()
height = app.winfo_height()
x = (app.winfo_screenwidth() // 2) - (width // 2)
y = (app.winfo_screenheight() // 2) - (height // 2)
app.geometry(f'{width}x{height}+{x}+{y}')


# --- 3. FONT & VARIABLES ---
main_font = ("Helvetica", 14)
bold_font = ("Helvetica", 14, "bold")

low_var = ctk.BooleanVar(value=True)
up_var = ctk.BooleanVar(value=True)
num_var = ctk.BooleanVar(value=True)
sym_var = ctk.BooleanVar(value=False)

# --- 4. WIDGETS ---
# Main Frame
main_frame = ctk.CTkFrame(app)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Title Label
title_label = ctk.CTkLabel(main_frame, text="Password Generator", font=("Helvetica", 20, "bold"))
title_label.pack(pady=(10, 20))

# --- Options Frame ---
options_frame = ctk.CTkFrame(main_frame)
options_frame.pack(pady=10, padx=10, fill="x")

length_label = ctk.CTkLabel(options_frame, text="Length: 12", font=main_font)
length_label.pack(pady=(10, 0))

slider = ctk.CTkSlider(options_frame, from_=8, to=32, number_of_steps=24, command=slider_event)
slider.set(12)
slider.pack(pady=10, padx=20, fill="x")

# Checkboxes in a grid
checkbox_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
checkbox_frame.pack(pady=10, padx=20, fill="x")
checkbox_frame.grid_columnconfigure((0, 1), weight=1)

low_check = ctk.CTkCheckBox(checkbox_frame, text="Lowercase", variable=low_var, font=main_font)
low_check.grid(row=0, column=0, sticky="w", pady=5)

up_check = ctk.CTkCheckBox(checkbox_frame, text="Uppercase", variable=up_var, font=main_font)
up_check.grid(row=0, column=1, sticky="w", pady=5)

num_check = ctk.CTkCheckBox(checkbox_frame, text="Numbers", variable=num_var, font=main_font)
num_check.grid(row=1, column=0, sticky="w", pady=5)

sym_check = ctk.CTkCheckBox(checkbox_frame, text="Symbols", variable=sym_var, font=main_font)
sym_check.grid(row=1, column=1, sticky="w", pady=5)

# --- Result Frame ---
result_frame = ctk.CTkFrame(main_frame)
result_frame.pack(pady=20, padx=10, fill="x")

result_entry = ctk.CTkEntry(result_frame, font=main_font, justify="center", width=250)
result_entry.pack(pady=(15, 10), padx=10, ipady=5, fill="x")

generate_btn = ctk.CTkButton(main_frame, text="Generate Password", command=generate_password, font=bold_font, height=40)
generate_btn.pack(pady=10, padx=10, fill="x")

copy_btn = ctk.CTkButton(main_frame, text="Copy", command=copy_to_clipboard, font=bold_font, height=40)
copy_btn.pack(pady=(0, 20), padx=10, fill="x")

# --- 5. START ---
app.mainloop()