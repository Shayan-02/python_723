from tkinter import messagebox


lst = [1, 2, 3]
try:
    print(lst[5])
except IndexError:
    messagebox.showerror("بیشتر از اعضا", "خانه مورد نظر در لیست وجود ندارد")