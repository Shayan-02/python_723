from tkinter import *


def show_fullname():
    fullname = fnameent.get() + " " + lnameent.get()
    fullnamelbl.config(text=fullname)



root = Tk()
# window = Tk()

root.title("fullname app")
root.geometry("600x300")
root.resizable(0, 0)

LBLFONT = ("vazir", 21, "bold")
ENTFONT = ("vazir", 18, "bold")

fnamelbl = Label(root, text="نام", font=LBLFONT).grid(row=0, column=0)
fnameent = Entry(root, font=ENTFONT, justify="center")
fnameent.grid(row=0, column=2)

lnamelbl = Label(root, text="نام خانوادگی", font=LBLFONT).grid(row=1, column=0)
lnameent = Entry(root, font=ENTFONT, justify="right")
lnameent.grid(row=1, column=2)

fullnamebtn = Button(root, text="نمایش نام", font=LBLFONT, width=8, bg="lightgreen", command=show_fullname).grid(row=2, column=1, pady=20)

fullnamelbl = Label(root, text="", font=LBLFONT)
fullnamelbl.grid(row=3, column=1)
root.mainloop()
# window.mainloop()