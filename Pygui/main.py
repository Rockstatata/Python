import customtkinter as ct

ct.set_appearance_mode("system")
ct.set_default_color_theme("dark-blue")

root = ct.CTk()
root.geometry("500x350 ")


def login():
    print("Test")


frame = ct.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ct.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = ct.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)
entry2 = ct.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = ct.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = ct.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()
