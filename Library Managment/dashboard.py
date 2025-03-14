import tkinter as tk
from tkinter import messagebox
from books import show_books_management as show_books_management_from_books
from members import show_members_management as show_members_management_from_members
from issue_return_books import show_issue_return_books as show_issue_return_books_from_issue_return_books
import sqlite3

def show_dashboard(master):
    
    for widget in master.winfo_children():
        widget.destroy()

    master.state('zoomed')
    dashboard_frame = tk.Frame(master, bg='white')
    dashboard_frame.pack(fill=tk.BOTH, expand=True)

    left_panel = tk.Frame(dashboard_frame, bg='lightgray', width=200)
    left_panel.pack(side=tk.LEFT, fill=tk.Y)


    global content_frame
    content_frame = tk.Frame(dashboard_frame, bg='white')
    content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    
    tk.Button(left_panel, text="Books Management", font=("Arial", 14), bg='#4b8cf9', fg='white', relief='flat',
              command=lambda: show_books_management(content_frame)).pack(fill=tk.X, padx=10, pady=10)
    
    tk.Button(left_panel, text="Members Management", font=("Arial", 14), bg='#4b8cf9', fg='white', relief='flat',
              command=lambda: show_members_management(content_frame)).pack(fill=tk.X, padx=10, pady=10)
    
    tk.Button(left_panel, text="Issue/Return Books", font=("Arial", 14), bg='#4b8cf9', fg='white', relief='flat',
              command=lambda: show_issue_return_management(content_frame)).pack(fill=tk.X, padx=10, pady=10)
    
    tk.Button(left_panel, text="Logout", command=lambda: logout(master), font=("Arial", 14), bg='#f94b4b', fg='white', relief='flat').pack(fill=tk.X, padx=10, pady=10)


    tk.Label(content_frame, text="Welcome to Library Management System!", font=("Arial", 24), bg='grey', fg='white').pack(pady=20)

    
    global search_frame
    search_frame = tk.Frame(content_frame, bg='white')  
    search_frame.pack(pady=10)

    global search_var
    search_var = tk.StringVar()  
    create_search_bar(content_frame)

def create_search_bar(frame):
    global search_frame
    search_frame = tk.Frame(frame, bg='white')
    search_frame.pack(pady=10)

    global search_var
    search_var = tk.StringVar()
    tk.Label(search_frame, text="Search:", font=("Arial", 14), bg='white').pack(side=tk.LEFT, padx=10)
    search_entry = tk.Entry(search_frame, textvariable=search_var, font=("Arial", 14), relief='solid')
    search_entry.pack(side=tk.LEFT, padx=10)

    tk.Button(search_frame, text="Search", font=("Arial", 14), bg='#4CAF50', fg='white', command=lambda: search_books(frame, search_var.get())).pack(side=tk.LEFT, padx=10)

def show_books_management(frame):
    show_books_management_from_books(frame)

def show_members_management(frame):
    show_members_management_from_members(frame)

def show_issue_return_management(frame):
    show_issue_return_books_from_issue_return_books(frame)

def search_books(frame, search_term):
    # Clear existing widgets in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    create_search_bar(frame)  

    try:
        with sqlite3.connect('Library.db') as db:
            cursor = db.cursor()
            query = "SELECT id, title, author, genre, year FROM Books WHERE title LIKE ? OR author LIKE ?"
            cursor.execute(query, (f"%{search_term}%", f"%{search_term}%"))
            books = cursor.fetchall()
            print(f"Books found: {books}")

            
            tk.Label(frame, text="Search Results", font=("Times New Roman", 18), bg='white').pack(pady=5)

            if not books:
                tk.Label(frame, text="No books found", font=("Times New Roman", 12), bg='white').pack(pady=5)
            else:
                table_frame = tk.Frame(frame, bg='white', width=600, height=200)
                table_frame.pack(pady=5, padx=10, anchor='n')  

            
                headers = ["ID", "Title", "Author", "Genre", "Year"]
                col_width = [5, 20, 20, 12, 8]  

                for col, (header, width) in enumerate(zip(headers, col_width)):
                    header_label = tk.Label(table_frame, text=header, font=("Times New Roman", 10, 'bold'), bg='lightgray', borderwidth=1, relief='solid', width=width)
                    header_label.grid(row=0, column=col, padx=1, pady=1, sticky='nsew')

                
                for row, book in enumerate(books, start=1):
                    for col, value in enumerate(book):
                        tk.Label(table_frame, text=value, font=("Times New Roman", 10), bg='white', borderwidth=1, relief='solid', width=col_width[col]).grid(row=row, column=col, padx=1, pady=1, sticky='nsew')


                for col in range(len(headers)):
                    table_frame.grid_columnconfigure(col, weight=1)
                for row in range(len(books) + 1):
                    table_frame.grid_rowconfigure(row, weight=1)

    except Exception as e:
        print(f"Error occurred: {e}")

def logout(master):
    response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if response:
        from login import create_login_frame
        create_login_frame(master)

if __name__ == "__main__":
    root = tk.Tk()
    show_dashboard(root)
    root.mainloop()
