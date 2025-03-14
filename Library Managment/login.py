import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from dashboard import show_dashboard

def create_login_frame(master):
    for widget in master.winfo_children():
        widget.destroy()

    
    original_image = Image.open("C:/Users/HP/OneDrive/Desktop/MP1/lib2.jpg")
    resized_image = original_image.resize((master.winfo_screenwidth(), master.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(resized_image)

    bg_label = tk.Label(master, image=bg_image)
    bg_label.image = bg_image 
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    
    title_label = tk.Label(master, text="Library Management System", font=("Times New Roman", 24, "bold"),
                       bg='#ff1297', fg='black', pady=10)
    title_label.place(x=0, y=0, width=master.winfo_screenwidth())
    title_label.config(anchor="center")
    
    admin_label = tk.Label(master, text="Admin Login", font=("Times New Roman", 18, "bold"), bg='#12beff', fg='black')
    admin_label.place(relx=0.85, rely=0.23, anchor=tk.CENTER, width=300,height=50)  # Adjust 'y' to position above the login frame

    auth_frame = tk.Frame(master, bg='white')
    auth_frame.place(relx=0.85, rely=0.5, anchor=tk.CENTER, width=300, height=350)

    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(auth_frame, text="Username:", font=("Times New Roman", 14), bg='white').pack(pady=(10, 5))
    tk.Entry(auth_frame, textvariable=username, font=("Times New Roman", 14), relief='solid').pack(pady=(10, 5))

    tk.Label(auth_frame, text="Password:", font=("Times New Roman", 14), bg='white').pack(pady=(20, 5))
    tk.Entry(auth_frame, textvariable=password, font=("Times New Roman", 14), relief='solid', show="*").pack(pady=(20, 5))

    tk.Button(auth_frame, text="Login", command=lambda: login(username, password, master), font=("Times New Roman", 14), fg="white", bg='#4b8cf9', relief='raised').pack(pady=(30, 20))

    register_label = tk.Label(auth_frame, text="Don't have an account? Register", font=("Times New Roman", 10),
                              fg="blue", bg="white", cursor="hand2")
    register_label.pack(pady=(5, 10))

    from register import show_registration_frame
    register_label.bind("<Button-1>", lambda e: show_registration_frame(master))

def login(username, password, master):
    if not username.get() or not password.get():
        messagebox.showerror("Error", "Username and Password cannot be empty.")
        return

    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Register WHERE username=? AND password=?', (username.get(), password.get()))
        if cursor.fetchone():
            from dashboard import show_dashboard
            show_dashboard(master)
        else:
            messagebox.showerror("Error", "Invalid Username or Password.")


if __name__ == "__main__":
    root = tk.Tk()
    
    # Set the size of the root window
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    
    create_login_frame(root)
    root.mainloop()
