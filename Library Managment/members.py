import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
from PIL import Image, ImageTk
import io

def init_db():
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Members (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            email TEXT,
                            phone TEXT,
                            address TEXT,
                            dob TEXT,
                            membership_type TEXT,
                            gender TEXT,
                            profile_picture BLOB
                          );''')
        db.commit()

def show_members_management(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="Members Management", font=("Times New Roman", 24), bg='white').pack(pady=20)

    btn_frame = tk.Frame(content_frame, bg='white')
    btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="Add Member", font=("Times New Roman", 14), bg='#4b8cf9', fg='white', command=lambda: add_member(content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Update Member", font=("Times New Roman", 14), bg='#4b8cf9', fg='white', command=lambda: update_member(content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Delete Member", font=("Times New Roman", 14), bg='#f44336', fg='white', command=lambda: delete_member(content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="View Members", font=("Times New Roman", 14), bg='#4CAF50', fg='white', command=lambda: view_members(content_frame)).pack(side=tk.LEFT, padx=10)

def add_member(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="Add New Member", font=("Times New Roman", 20), bg='white').pack(pady=20)
    form_frame = tk.Frame(content_frame, bg='white')
    form_frame.pack(pady=10)

    name_var = tk.StringVar()
    email_var = tk.StringVar()
    phone_var = tk.StringVar()
    address_var = tk.StringVar()
    dob_var = tk.StringVar()
    membership_type_var = tk.StringVar()
    gender_var = tk.StringVar()
    profile_picture_var = tk.StringVar()

    tk.Label(form_frame, text="Name:", font=("Times New Roman", 14), bg='white').grid(row=0, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=name_var, font=("Times New Roman", 14), relief='solid').grid(row=0, column=1, pady=10)

    tk.Label(form_frame, text="Email:", font=("Times New Roman", 14), bg='white').grid(row=1, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=email_var, font=("Times New Roman", 14), relief='solid').grid(row=1, column=1, pady=10)

    tk.Label(form_frame, text="Phone:", font=("Times New Roman", 14), bg='white').grid(row=2, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=phone_var, font=("Times New Roman", 14), relief='solid').grid(row=2, column=1, pady=10)

    tk.Label(form_frame, text="Address:", font=("Times New Roman", 14), bg='white').grid(row=3, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=address_var, font=("Times New Roman", 14), relief='solid').grid(row=3, column=1, pady=10)

    tk.Label(form_frame, text="DOB:", font=("Times New Roman", 14), bg='white').grid(row=4, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=dob_var, font=("Times New Roman", 14), relief='solid').grid(row=4, column=1, pady=10)

    tk.Label(form_frame, text="Membership Type:", font=("Times New Roman", 14), bg='white').grid(row=5, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=membership_type_var, font=("Times New Roman", 14), relief='solid').grid(row=5, column=1, pady=10)

    tk.Label(form_frame, text="Gender:", font=("Times New Roman", 14), bg='white').grid(row=6, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=gender_var, font=("Times New Roman", 14), relief='solid').grid(row=6, column=1, pady=10)

    tk.Label(form_frame, text="Profile Picture:", font=("Times New Roman", 14), bg='white').grid(row=7, column=0, pady=10, sticky=tk.E)
    tk.Button(form_frame, text="Upload Photo", font=("Times New Roman", 14), bg='#4CAF50', fg='white', command=lambda: upload_photo(profile_picture_var)).grid(row=7, column=1, pady=10)

    action_frame = tk.Frame(content_frame, bg='white')
    action_frame.pack(pady=20)

    tk.Button(action_frame, text="Submit", font=("Times New Roman", 14), bg='#4CAF50', fg='white', command=lambda: submit_member(name_var, email_var, phone_var, address_var, dob_var, membership_type_var, gender_var, profile_picture_var, content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(action_frame, text="Back", font=("Times New Roman", 14), bg='#4b8cf9', fg='white', command=lambda: show_members_management(content_frame)).pack(side=tk.LEFT, padx=10)

def upload_photo(profile_picture_var):
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        profile_picture_var.set(file_path)

def submit_member(name, email, phone, address, dob, membership_type, gender, profile_picture_var, content_frame):
    profile_picture_data = None
    if profile_picture_var.get():
        with open(profile_picture_var.get(), 'rb') as file:
            profile_picture_data = file.read()

    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('''INSERT INTO Members (name, email, phone, address, dob, membership_type, gender, profile_picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (name.get(), email.get(), phone.get(), address.get(), dob.get(), membership_type.get(), gender.get(), profile_picture_data))
        db.commit()
    messagebox.showinfo("Success", "Member added successfully.")
    view_members(content_frame)

def update_member(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="Update Member", font=("Times New Roman", 20), bg='white').pack(pady=20)
    form_frame = tk.Frame(content_frame, bg='white')
    form_frame.pack(pady=10)

    id_var = tk.StringVar()
    name_var = tk.StringVar()
    email_var = tk.StringVar()
    phone_var = tk.StringVar()
    address_var = tk.StringVar()
    dob_var = tk.StringVar()
    membership_type_var = tk.StringVar()
    gender_var = tk.StringVar()

    tk.Label(form_frame, text="Member ID:", font=("Times New Roman", 14), bg='white').grid(row=0, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=id_var, font=("Times New Roman", 14), relief='solid').grid(row=0, column=1, pady=10)

    tk.Label(form_frame, text="Name:", font=("Times New Roman", 14), bg='white').grid(row=1, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=name_var, font=("Times New Roman", 14), relief='solid').grid(row=1, column=1, pady=10)

    tk.Label(form_frame, text="Email:", font=("Times New Roman", 14), bg='white').grid(row=2, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=email_var, font=("Times New Roman", 14), relief='solid').grid(row=2, column=1, pady=10)

    tk.Label(form_frame, text="Phone:", font=("Times New Roman", 14), bg='white').grid(row=3, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=phone_var, font=("Times New Roman", 14), relief='solid').grid(row=3, column=1, pady=10)

    tk.Label(form_frame, text="Address:", font=("Times New Roman", 14), bg='white').grid(row=4, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=address_var, font=("Times New Roman", 14), relief='solid').grid(row=4, column=1, pady=10)

    tk.Label(form_frame, text="DOB:", font=("Times New Roman", 14), bg='white').grid(row=5, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=dob_var, font=("Times New Roman", 14), relief='solid').grid(row=5, column=1, pady=10)

    tk.Label(form_frame, text="Membership Type:", font=("Times New Roman", 14), bg='white').grid(row=6, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=membership_type_var, font=("Times New Roman", 14), relief='solid').grid(row=6, column=1, pady=10)

    tk.Label(form_frame, text="Gender:", font=("Times New Roman", 14), bg='white').grid(row=7, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=gender_var, font=("Times New Roman", 14), relief='solid').grid(row=7, column=1, pady=10)

    action_frame = tk.Frame(content_frame, bg='white')
    action_frame.pack(pady=20)

    tk.Button(action_frame, text="Submit", font=("Times New Roman", 14), bg='#4CAF50', fg='white', command=lambda: submit_update(id_var, name_var, email_var, phone_var, address_var, dob_var, membership_type_var, gender_var, content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(action_frame, text="Back", font=("Times New Roman", 14), bg='#4b8cf9', fg='white', command=lambda: show_members_management(content_frame)).pack(side=tk.LEFT, padx=10)

def submit_update(id_var, name, email, phone, address, dob, membership_type, gender, content_frame):
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('''UPDATE Members SET name=?, email=?, phone=?, address=?, dob=?, membership_type=?, gender=? WHERE id=?''',
                       (name.get(), email.get(), phone.get(), address.get(), dob.get(), membership_type.get(), gender.get(), id_var.get()))
        db.commit()
    messagebox.showinfo("Success", "Member updated successfully.")
    view_members(content_frame)

def delete_member(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="Delete Member", font=("Times New Roman", 20), bg='white').pack(pady=20)
    form_frame = tk.Frame(content_frame, bg='white')
    form_frame.pack(pady=10)

    id_var = tk.StringVar()

    tk.Label(form_frame, text="Member ID:", font=("Times New Roman", 14), bg='white').grid(row=0, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=id_var, font=("Times New Roman", 14), relief='solid').grid(row=0, column=1, pady=10)

    action_frame = tk.Frame(content_frame, bg='white')
    action_frame.pack(pady=20)

    tk.Button(action_frame, text="Delete", font=("Times New Roman", 14), bg='#f44336', fg='white', command=lambda: submit_delete(id_var, content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(action_frame, text="Back", font=("Times New Roman", 14), bg='#4b8cf9', fg='white', command=lambda: show_members_management(content_frame)).pack(side=tk.LEFT, padx=10)

def submit_delete(id_var, content_frame):
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('DELETE FROM Members WHERE id=?', (id_var.get(),))
        db.commit()
    messagebox.showinfo("Success", "Member deleted successfully.")
    view_members(content_frame)

def view_members(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Members")
        members = cursor.fetchall()

    tk.Label(content_frame, text="View Members", font=("Times New Roman", 24), bg='white').pack(pady=20)

    if not members:
        tk.Label(content_frame, text="No members found.", font=("Times New Roman", 16), bg='white').pack(pady=20)
        return

    table_frame = tk.Frame(content_frame, bg='white')
    table_frame.pack(pady=10)

    headers = ["ID", "Name", "Email", "Phone", "Address", "DOB", "Membership Type", "Gender"]
    # Create headers
    for col, header in enumerate(headers):
        tk.Label(table_frame, text=header, font=("Times New Roman", 14, 'bold'), bg='white', borderwidth=1, relief='solid', padx=10, pady=5).grid(row=0, column=col, padx=1, pady=1, sticky='nsew')


    for row, member in enumerate(members, start=1):
        for col, value in enumerate(member[:-1]):  # Exclude profile_picture
            tk.Label(table_frame, text=value, font=("Times New Roman", 14), bg='white', borderwidth=1, relief='solid', padx=10, pady=5).grid(row=row, column=col, padx=1, pady=1, sticky='nsew')

    for col in range(len(headers)):
        table_frame.grid_columnconfigure(col, weight=1)
    for row in range(len(members) + 1):
        table_frame.grid_rowconfigure(row, weight=1)

    back_frame = tk.Frame(content_frame, bg='white')
    back_frame.pack(pady=20)

    tk.Button(back_frame, text="Back", font=("Times New Roman", 14), bg='#4b8cf9', fg='white', command=lambda: show_members_management(content_frame)).pack(pady=10)

def back_to_main(content_frame):
    pass

def main():
    root = tk.Tk()
    root.title("Library Management System")

    content_frame = tk.Frame(root, bg='white')
    content_frame.pack(expand=True, fill=tk.BOTH)

    init_db()
    show_members_management(content_frame)

    root.mainloop()

if __name__ == "__main__":
    main()
