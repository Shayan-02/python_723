from tkinter import *
from tkinter import messagebox, filedialog
from random import *

def addtofile():
  name = nameent.get()
  with open("./j16/test.txt", "a") as f:
    f.write(f"{name}\n")

def shufflename(num):
  winners = []
  for i in range(num):
    with open("./j16/test.txt", encoding="utf-8") as f:
      winners.append(choice(f.readlines()))
  messagebox.showinfo("برندگان", winners)

LBLFONT= ("vazir", 20, "bold")
ENTFONT= ("vazir", 18, "bold")

root = Tk()
root.geometry("350x400")

namelbl = Label(root, text="نام شرکت کنندگان", font=LBLFONT).pack()

nameent = Entry(root, font=ENTFONT)
nameent.pack()

submitbtn = Button(root, text="اضافه به فایل", font=LBLFONT, command=lambda : addtofile())
submitbtn.pack(pady=20)

countlbl = Label(root, text="تعداد برندگان ", font=LBLFONT).pack()

countent = Entry(root, font=ENTFONT)
countent.pack()

shufflebtn = Button(root, text="انتخاب از فایل", font=LBLFONT, command=lambda : shufflename(int(countent.get())))
shufflebtn.pack(pady=20)

root.mainloop()