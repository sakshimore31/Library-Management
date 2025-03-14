import tkinter as tk
from tkinter import messagebox
import sqlite3

def init_db():
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT,
                            author TEXT,
                            genre TEXT,
                            year INTEGER
                          );''')
        db.commit()

def insert_sample_data():
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()

        sample_data = [
            ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960),
            ('1984', 'George Orwell', 'Dystopian', 1949),
            ('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 1925),
            ('Pride and Prejudice', 'Jane Austen', 'Romance', 1813),
            ('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951)
        ]

        for data in sample_data:
            cursor.execute("SELECT * FROM Books WHERE title = ? AND author = ?", (data[0], data[1]))
            if cursor.fetchone() is None:
                cursor.execute('''INSERT INTO Books (title, author, genre, year) VALUES (?, ?, ?, ?)''', data)
        
        db.commit()

def show_books_management(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="Books Management", font=("Times New Roman", 24), bg='white').pack(pady=20)

    btn_frame = tk.Frame(content_frame, bg='white')
    btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="Add Book", font=("Times New Roman", 14), bg='#4b8cf9', fg='white', command=lambda: add_book(content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Update Book", font=("Times New Roman", 14), bg='#4b8cf9', fg='white', command=lambda: update_book(content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Delete Book", font=("Times New Roman", 14), bg='#f44336', fg='white', command=lambda: delete_book(content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="View Books", font=("Times New Roman", 14), bg='#4CAF50', fg='white', command=lambda: view_books(content_frame)).pack(side=tk.LEFT, padx=10)

def add_book(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="Add New Book", font=("Times New Roman", 20), bg='white').pack(pady=20)
    form_frame = tk.Frame(content_frame, bg='white')
    form_frame.pack(pady=10)

    title_var = tk.StringVar()
    author_var = tk.StringVar()
    genre_var = tk.StringVar()
    year_var = tk.StringVar()

    tk.Label(form_frame, text="Title:", font=("Times New Roman", 14), bg='white').grid(row=0, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=title_var, font=("Times New Roman", 14), relief='solid').grid(row=0, column=1, pady=10)

    tk.Label(form_frame, text="Author:", font=("Times New Roman", 14), bg='white').grid(row=1, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=author_var, font=("Times New Roman", 14), relief='solid').grid(row=1, column=1, pady=10)

    tk.Label(form_frame, text="Genre:", font=("Times New Roman", 14), bg='white').grid(row=2, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=genre_var, font=("Times New Roman", 14), relief='solid').grid(row=2, column=1, pady=10)

    tk.Label(form_frame, text="Year:", font=("Times New Roman", 14), bg='white').grid(row=3, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=year_var, font=("Times New Roman", 14), relief='solid').grid(row=3, column=1, pady=10)

    button_frame = tk.Frame(content_frame, bg='white')
    button_frame.pack(pady=20)
    tk.Button(button_frame, text="Submit", font=("Times New Roman", 14), bg='#4CAF50', fg='white', command=lambda: submit_book(title_var, author_var, genre_var, year_var, content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Back", font=("Times New Roman", 14), bg='lightgrey', fg='black', command=lambda: show_books_management(content_frame)).pack(side=tk.LEFT, padx=10)

def submit_book(title, author, genre, year, content_frame):
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('''INSERT INTO Books (title, author, genre, year) VALUES (?, ?, ?, ?)''', (title.get(), author.get(), genre.get(), year.get()))
        db.commit()
    messagebox.showinfo("Success", "Book added successfully.")
    view_books(content_frame)

def update_book(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="Update Book", font=("Times New Roman", 20), bg='white').pack(pady=20)
    form_frame = tk.Frame(content_frame, bg='white')
    form_frame.pack(pady=10)

    id_var = tk.StringVar()
    title_var = tk.StringVar()
    author_var = tk.StringVar()
    genre_var = tk.StringVar()
    year_var = tk.StringVar()

    tk.Label(form_frame, text="Book ID:", font=("Times New Roman", 14), bg='white').grid(row=0, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=id_var, font=("Times New Roman", 14), relief='solid').grid(row=0, column=1, pady=10)

    tk.Label(form_frame, text="Title:", font=("Times New Roman", 14), bg='white').grid(row=1, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=title_var, font=("Times New Roman", 14), relief='solid').grid(row=1, column=1, pady=10)

    tk.Label(form_frame, text="Author:", font=("Times New Roman", 14), bg='white').grid(row=2, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=author_var, font=("Times New Roman", 14), relief='solid').grid(row=2, column=1, pady=10)

    tk.Label(form_frame, text="Genre:", font=("Times New Roman", 14), bg='white').grid(row=3, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=genre_var, font=("Times New Roman", 14), relief='solid').grid(row=3, column=1, pady=10)

    tk.Label(form_frame, text="Year:", font=("Times New Roman", 14), bg='white').grid(row=4, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=year_var, font=("Times New Roman", 14), relief='solid').grid(row=4, column=1, pady=10)

    button_frame = tk.Frame(content_frame, bg='white')
    button_frame.pack(pady=20)
    tk.Button(button_frame, text="Update", font=("Times New Roman", 14), bg='#4CAF50', fg='white', command=lambda: submit_update(id_var, title_var, author_var, genre_var, year_var, content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Back", font=("Times New Roman", 14), bg='lightgrey', fg='black', command=lambda: show_books_management(content_frame)).pack(side=tk.LEFT, padx=10)

def submit_update(book_id, title, author, genre, year, content_frame):
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('''UPDATE Books SET title = ?, author = ?, genre = ?, year = ? WHERE id = ?''',
                       (title.get(), author.get(), genre.get(), year.get(), book_id.get()))
        db.commit()
    messagebox.showinfo("Success", "Book updated successfully.")
    view_books(content_frame)

def delete_book(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="Delete Book", font=("Times New Roman", 20), bg='white').pack(pady=20)
    form_frame = tk.Frame(content_frame, bg='white')
    form_frame.pack(pady=10)

    id_var = tk.StringVar()

    tk.Label(form_frame, text="Book ID:", font=("Times New Roman", 14), bg='white').grid(row=0, column=0, pady=10, sticky=tk.E)
    tk.Entry(form_frame, textvariable=id_var, font=("Times New Roman", 14), relief='solid').grid(row=0, column=1, pady=10)

    button_frame = tk.Frame(content_frame, bg='white')
    button_frame.pack(pady=20)
    tk.Button(button_frame, text="Delete", font=("Times New Roman", 14), bg='#f44336', fg='white', command=lambda: submit_delete(id_var, content_frame)).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Back", font=("Times New Roman", 14), bg='lightgrey', fg='black', command=lambda: show_books_management(content_frame)).pack(side=tk.LEFT, padx=10)

def submit_delete(book_id, content_frame):
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('''DELETE FROM Books WHERE id = ?''', (book_id.get(),))
        db.commit()
    messagebox.showinfo("Success", "Book deleted successfully.")
    view_books(content_frame)

def view_books(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()

    tk.Label(content_frame, text="View Books", font=("Times New Roman", 24), bg='white').pack(pady=20)

    table_frame = tk.Frame(content_frame, bg='white')
    table_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    headers = ["ID", "Title", "Author", "Genre", "Year"]
    for col, header in enumerate(headers):
        tk.Label(table_frame, text=header, font=("Times New Roman", 14, 'bold'), bg='lightgray', borderwidth=1, relief='solid', width=15).grid(row=0, column=col, padx=2, pady=2)

    for row, book in enumerate(books, start=1):
        for col, value in enumerate(book):
            tk.Label(table_frame, text=value, font=("Times New Roman", 12), bg='white', borderwidth=1, relief='solid', width=15).grid(row=row, column=col, padx=2, pady=2)

    tk.Button(content_frame, text="Back", font=("Times New Roman", 14), bg='lightgrey', fg='black', command=lambda: show_books_management(content_frame)).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Library Management System")

    init_db()
    insert_sample_data()

    content_frame = tk.Frame(root, bg='white')
    content_frame.pack(fill=tk.BOTH, expand=True)

    show_books_management(content_frame)

    root.mainloop()
