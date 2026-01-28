from tkinter import messagebox


try:
    with open("./1.txt") as f:
        f.read()
except FileNotFoundError:
    a = input("file peyda nashod. aya mikhahid file sakhte shavad? ")
    if a.lower() == "y":
        messagebox.showinfo("وجود فایل", "فایل پیدا نشد، یک فایل جدید به جای آن ساخته شد")
        open("./1.txt", "a")