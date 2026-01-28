from tkinter import *
from tkinter import messagebox
from random import randint
from sqlite3 import *

con = connect("./bank2.db")
c = con.cursor()
sql = """
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRYMARY KEY,
cardNumber INTEGER,
u_name VARCHAR (60) NOT NULL,
u_balance INTEGER
);
"""
c.execute(sql)
con.commit()

def create_user():
    i = 1
    name = name_ent.get()
    balance = balance_ent.get()
    cNumber = randint(1000, 9999)
    c.execute(
                "INSERT INTO users (id, cardNumber, u_name, u_balance) VALUES (?, ?, ?, ?)",
                (i, cNumber, name, balance))
    i += 1
    try:
        con.commit()
        messagebox.showinfo("ساخت حساب", "حساب جدید با موفقیت ساخته شد")
    except Exception:
        messagebox.showerror('خطای ساخت حساب', 'حساب کاربری ساخته نشد')



PRIMARY_FONT = ("vazir", 20, "bold")
SECONDRY_FONT = ("vazir", 16, "bold")

asghar = Tk()
asghar.title("bank account")
asghar.geometry('400x400')
asghar.resizable(width=False, height=False)


name_lbl = Label(asghar, text="نام", font=PRIMARY_FONT)
name_lbl.pack(pady=20)

name_ent = Entry(asghar, font=SECONDRY_FONT)
name_ent.pack()

balance_lbl = Label(asghar, text="موجودی اولیه", font=PRIMARY_FONT)
balance_lbl.pack(pady=20)

balance_ent = Entry(asghar, font=SECONDRY_FONT)
balance_ent.pack()

create_btn = Button(asghar, text="ساخت حساب", font=PRIMARY_FONT, bg="lightgreen", command=create_user)
create_btn.pack(pady=20)
asghar.mainloop()
con.close()