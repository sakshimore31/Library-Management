import tkinter as tk
from tkinter import messagebox
from login import create_login_frame
import sqlite3
import re
from PIL import Image, ImageTk
from dashboard import show_dashboard

def show_registration_frame(master):
    for widget in master.winfo_children():
        widget.destroy()

    original_image = Image.open("C:/Users/HP/OneDrive/Desktop/MP1/img01.jpg")
    resized_image = original_image.resize((master.winfo_screenwidth(), master.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(resized_image)
    bg_label = tk.Label(master, image=bg_image)
    
    bg_label.image = bg_image  
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    title_label = tk.Label(master, text="Library Management System", font=("Times New Roman", 24, "bold"),
                           bg='#000000', fg='#ffffff', pady=10)
    title_label.place(x=0, y=0, width=master.winfo_screenwidth()) 
    title_label.config(anchor="center")
    shadow_frame = tk.Frame(master, bg='#e0e0e0', bd=5, relief='raised')
    shadow_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=460, height=640)
    auth_frame = tk.Frame(master, bg='white', bd=2, relief='flat')
    auth_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=450, height=620)
    
    padding_y = 15

    fullname = tk.StringVar()
    dob = tk.StringVar()
    gender = tk.StringVar(value="Male")
    address = tk.StringVar()
    email = tk.StringVar()
    mobile = tk.StringVar()
    usertype = tk.StringVar(value="School")
    username = tk.StringVar()
    password = tk.StringVar()

   
    tk.Label(auth_frame, text="Full Name:", font=("Times New Roman", 12), bg='white').grid(row=0, column=0, padx=10, pady=padding_y, sticky=tk.W)
    tk.Entry(auth_frame, textvariable=fullname, font=("Times New Roman", 12), relief='groove', bd=2).grid(row=0, column=1, padx=10, pady=padding_y, sticky=tk.EW)

   
    tk.Label(auth_frame, text="DOB (DD-MM-YYYY):", font=("Times New Roman", 12), bg='white').grid(row=1, column=0, padx=10, pady=padding_y, sticky=tk.W)
    tk.Entry(auth_frame, textvariable=dob, font=("Times New Roman", 12), relief='groove', bd=2).grid(row=1, column=1, padx=10, pady=padding_y, sticky=tk.EW)

    
    tk.Label(auth_frame, text="Gender:", font=("Times New Roman", 12), bg='white').grid(row=2, column=0, padx=10, pady=padding_y, sticky=tk.W)
    gender_frame = tk.Frame(auth_frame, bg='white')
    gender_frame.grid(row=2, column=1, padx=10, pady=padding_y, sticky=tk.EW)
    tk.Radiobutton(gender_frame, text="Male", variable=gender, value="Male", bg='white').pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(gender_frame, text="Female", variable=gender, value="Female", bg='white').pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(gender_frame, text="Other", variable=gender, value="Other", bg='white').pack(side=tk.LEFT, padx=5)

    
    tk.Label(auth_frame, text="Address:", font=("Times New Roman", 12), bg='white').grid(row=3, column=0, padx=10, pady=padding_y, sticky=tk.W)
    tk.Entry(auth_frame, textvariable=address, font=("Times New Roman", 12), relief='groove', bd=2).grid(row=3, column=1, padx=10, pady=padding_y, sticky=tk.EW)
    
    tk.Label(auth_frame, text="E-mail:", font=("Times New Roman", 12), bg='white').grid(row=4, column=0, padx=10, pady=padding_y, sticky=tk.W)
    tk.Entry(auth_frame, textvariable=email, font=("Times New Roman", 12), relief='groove', bd=2).grid(row=4, column=1, padx=10, pady=padding_y, sticky=tk.EW)

    tk.Label(auth_frame, text="Mobile Number:", font=("Times New Roman", 12), bg='white').grid(row=5, column=0, padx=10, pady=padding_y, sticky=tk.W)
    tk.Entry(auth_frame, textvariable=mobile, font=("Times New Roman", 12), relief='groove', bd=2).grid(row=5, column=1, padx=10, pady=padding_y, sticky=tk.EW)

    tk.Label(auth_frame, text="Usertype:", font=("Times New Roman", 12), bg='white').grid(row=6, column=0, padx=10, pady=padding_y, sticky=tk.W)
    usertype_frame = tk.Frame(auth_frame, bg='white')
    usertype_frame.grid(row=6, column=1, padx=10, pady=padding_y, sticky=tk.EW)
    tk.Radiobutton(usertype_frame, text="School", variable=usertype, value="School", bg='white').pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(usertype_frame, text="University", variable=usertype, value="University", bg='white').pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(usertype_frame, text="Employee", variable=usertype, value="Employee", bg='white').pack(side=tk.LEFT, padx=5)


    tk.Label(auth_frame, text="Username:", font=("Times New Roman", 12), bg='white').grid(row=7, column=0, padx=10, pady=padding_y, sticky=tk.W)
    tk.Entry(auth_frame, textvariable=username, font=("Times New Roman", 12), relief='groove', bd=2).grid(row=7, column=1, padx=10, pady=padding_y, sticky=tk.EW)

    
    tk.Label(auth_frame, text="Password:", font=("Times New Roman", 12), bg='white').grid(row=8, column=0, padx=10, pady=padding_y, sticky=tk.W)
    tk.Entry(auth_frame, textvariable=password, font=("Times New Roman", 12), relief='groove', bd=2, show="*").grid(row=8, column=1, padx=10, pady=padding_y, sticky=tk.EW)

    
    tk.Button(auth_frame, text="Register", command=lambda: register(fullname, dob, gender, address, email, mobile, usertype, username, password), font=("Times New Roman", 14), fg="white", bg='#4b8cf9', relief='raised').grid(row=9, column=0, columnspan=2, pady=20)

    
    login_label = tk.Label(auth_frame, text="Already have an account? Login", font=("Times New Roman", 10),
                           fg="blue", bg="white", cursor="hand2")
    login_label.grid(row=10, column=0, columnspan=2, pady=10)

    
    login_label.bind("<Button-1>", lambda e: create_login_frame(master))

def register(fullname, dob, gender, address, email, mobile, usertype, username, password):
    if not username.get() or not password.get():
        messagebox.showerror("Error", "Username and Password cannot be empty.")
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email.get()):
        messagebox.showerror("Error", "Invalid Email format.")
        return

    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('INSERT INTO Register(fullname, dob, gender, address, email, mobile, usertype, username, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (fullname.get(), dob.get(), gender.get(), address.get(), email.get(), mobile.get(), usertype.get(), username.get(), password.get()))
        db.commit()

    messagebox.showinfo("Success", "Registration Successful.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Registration")
    root.geometry("1024x768")  
    show_registration_frame(root)

    root.mainloop()
