import tkinter as tk
from tkinter import messagebox
import sqlite3

def init_db():
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Transactions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            book_id INTEGER,
                            member_id INTEGER,
                            issue_date DATE,
                            return_date DATE,
                            status TEXT,
                            FOREIGN KEY(book_id) REFERENCES Books(id),
                            FOREIGN KEY(member_id) REFERENCES Members(id)
                          );''')
        db.commit()

def show_issue_return_books(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    
    tk.Label(content_frame, text="Issue/Return Books", font=("Times New Roman", 24), bg='white').pack(pady=20)
    btn_frame = tk.Frame(content_frame, bg='white')
    btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="Issue Book", font=("Times New Roman", 14), bg='#4b8cf9', fg='white', command=lambda: issue_book(content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Return Book", font=("Times New Roman", 14), bg='#4CAF50', fg='white', command=lambda: return_book(content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Search Transactions", font=("Times New Roman", 14), bg='#f0ad4e', fg='white', command=lambda: search_transactions(content_frame)).pack(side=tk.LEFT, padx=10)

def issue_book(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()


    tk.Label(content_frame, text="Issue Book", font=("Times New Roman", 20), bg='white').pack(pady=20)
    form_frame = tk.Frame(content_frame, bg='white')
    form_frame.pack(pady=10)

    book_id_var = tk.StringVar()
    member_id_var = tk.StringVar()
    issue_date_var = tk.StringVar()

    tk.Label(form_frame, text="Book ID:", font=("Times New Roman", 14), bg='white').grid(row=0, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=book_id_var, font=("Times New Roman", 14), relief='solid').grid(row=0, column=1, pady=10)

    tk.Label(form_frame, text="Member ID:", font=("Times New Roman", 14), bg='white').grid(row=1, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=member_id_var, font=("Times New Roman", 14), relief='solid').grid(row=1, column=1, pady=10)

    tk.Label(form_frame, text="Issue Date:", font=("Times New Roman", 14), bg='white').grid(row=2, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=issue_date_var, font=("Times New Roman", 14), relief='solid').grid(row=2, column=1, pady=10)

    btn_frame = tk.Frame(content_frame, bg='white')
    btn_frame.pack(pady=20)
    tk.Button(btn_frame, text="Submit", font=("Times New Roman", 14), bg='#4CAF50', fg='white', command=lambda: submit_issue(book_id_var, member_id_var, issue_date_var)).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Back", font=("Times New Roman", 14), bg='#f0ad4e', fg='white', command=lambda: show_issue_return_books(content_frame)).pack(side=tk.LEFT, padx=10)

def submit_issue(book_id, member_id, issue_date):
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('''INSERT INTO Transactions (book_id, member_id, issue_date, status) VALUES (?, ?, ?, ?)''',
                       (book_id.get(), member_id.get(), issue_date.get(), 'Issued'))
        db.commit()
        transaction_id = cursor.lastrowid  
    messagebox.showinfo("Success", f"Book issued successfully.\nTransaction ID: {transaction_id}")

def return_book(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()


    tk.Label(content_frame, text="Return Book", font=("Times New Roman", 20), bg='white').pack(pady=20)
    form_frame = tk.Frame(content_frame, bg='white')
    form_frame.pack(pady=10)

    transaction_id_var = tk.StringVar()
    return_date_var = tk.StringVar()

    tk.Label(form_frame, text="Transaction ID:", font=("Times New Roman", 14), bg='white').grid(row=0, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=transaction_id_var, font=("Times New Roman", 14), relief='solid').grid(row=0, column=1, pady=10)

    tk.Label(form_frame, text="Return Date:", font=("Times New Roman", 14), bg='white').grid(row=1, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=return_date_var, font=("Times New Roman", 14), relief='solid').grid(row=1, column=1, pady=10)
    
    btn_frame = tk.Frame(content_frame, bg='white')
    btn_frame.pack(pady=20)
    tk.Button(btn_frame, text="Submit", font=("Times New Roman", 14), bg='#4CAF50', fg='white', command=lambda: submit_return(transaction_id_var, return_date_var)).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Back", font=("Times New Roman", 14), bg='#f0ad4e', fg='white', command=lambda: show_issue_return_books(content_frame)).pack(side=tk.LEFT, padx=10)

def submit_return(transaction_id, return_date):
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('''UPDATE Transactions SET return_date = ?, status = ? WHERE id = ?''', (return_date.get(), 'Returned', transaction_id.get()))
        db.commit()
    messagebox.showinfo("Success", "Book returned successfully.")

def search_transactions(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    
    tk.Label(content_frame, text="Search Transactions", font=("Times New Roman", 20), bg='white').pack(pady=20)
    form_frame = tk.Frame(content_frame, bg='white')
    form_frame.pack(pady=10)

    search_type = tk.StringVar(value="member")  # Default search by member ID

    tk.Radiobutton(form_frame, text="By Member ID", variable=search_type, value="member", font=("Times New Roman", 14), bg='white').grid(row=0, column=0, pady=10, sticky=tk.W)
    tk.Radiobutton(form_frame, text="By Book ID", variable=search_type, value="book", font=("Times New Roman", 14), bg='white').grid(row=0, column=1, pady=10, sticky=tk.W)
    tk.Radiobutton(form_frame, text="By Date Range", variable=search_type, value="date", font=("Times New Roman", 14), bg='white').grid(row=0, column=2, pady=10, sticky=tk.W)

    search_var = tk.StringVar()

    tk.Label(form_frame, text="Search Query:", font=("Times New Roman", 14), bg='white').grid(row=1, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=search_var, font=("Times New Roman", 14), relief='solid').grid(row=1, column=1, pady=10)

    tk.Label(form_frame, text="Start Date (YYYY-MM-DD):", font=("Times New Roman", 14), bg='white').grid(row=2, column=0, pady=10, sticky=tk.E)
    start_date_var = tk.StringVar()
    tk.Entry(form_frame, textvariable=start_date_var, font=("Times New Roman", 14), relief='solid').grid(row=2, column=1, pady=10)

    tk.Label(form_frame, text="End Date (YYYY-MM-DD):", font=("Times New Roman", 14), bg='white').grid(row=3, column=0, pady=10, sticky=tk.E)
    end_date_var = tk.StringVar()
    tk.Entry(form_frame, textvariable=end_date_var, font=("Times New Roman", 14), relief='solid').grid(row=3, column=1, pady=10)

    btn_frame = tk.Frame(content_frame, bg='white')
    btn_frame.pack(pady=20)
    tk.Button(btn_frame, text="Search", font=("Times New Roman", 14), bg='#4CAF50', fg='white', command=lambda: display_transactions(content_frame, search_type, search_var, start_date_var, end_date_var)).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Back", font=("Times New Roman", 14), bg='#f0ad4e', fg='white', command=lambda: show_issue_return_books(content_frame)).pack(side=tk.LEFT, padx=10)

def display_transactions(content_frame, search_type, search_var, start_date_var, end_date_var):
    query = ''
    params = []
    
    if search_type.get() == "member":
        query = '''SELECT * FROM Transactions WHERE member_id=?'''
        params = [search_var.get()]
    elif search_type.get() == "book":
        query = '''SELECT * FROM Transactions WHERE book_id=?'''
        params = [search_var.get()]
    elif search_type.get() == "date":
        query = '''SELECT * FROM Transactions WHERE issue_date BETWEEN ? AND ?'''
        params = [start_date_var.get(), end_date_var.get()]

    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute(query, params)
        transactions = cursor.fetchall()

    if not transactions:
        messagebox.showinfo("No Records", "No transactions found for the given criteria.")
        return

    
    for widget in content_frame.winfo_children():
        widget.destroy()

    
    tk.Label(content_frame, text="Transaction History", font=("Times New Roman", 20), bg='white').pack(pady=20)
    for transaction in transactions:
        tk.Label(content_frame, text=f"Transaction ID: {transaction[0]}, Book ID: {transaction[1]}, Member ID: {transaction[2]}, Issue Date: {transaction[3]}, Return Date: {transaction[4]}, Status: {transaction[5]}", font=("Times New Roman", 14), bg='white').pack(pady=5)

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    content_frame = tk.Frame(root, bg='white')
    content_frame.pack(fill=tk.BOTH, expand=True)
    show_issue_return_books(content_frame)
    root.mainloop()
