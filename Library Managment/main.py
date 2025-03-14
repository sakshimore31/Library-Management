import tkinter as tk
from login import create_login_frame
from db import init_db
from dashboard import show_dashboard  

def main():
    master = tk.Tk()
    master.geometry("1920x1080")
    master.title("Library Management System")

    init_db()
    create_login_frame(master)  

    master.mainloop()

if __name__ == "__main__":
    main()
