from tkinter import *


def show_fullname():
    fullname = fnameent.get() + " " + lnameent.get()
    fullnamelbl.config(text=f"{fullname} خوش آمدید")


root = Tk()
# window = Tk()

root.title("fullname app")
root.geometry("500x400")

LBLFONT = ("vazir", 21, "bold")
ENTFONT = ("vazir", 18, "bold")

fnamelbl = Label(root, text="نام", font=("vazir", 21, "bold")).place(x=450, y=10)
fnameent = Entry(root, font=ENTFONT, justify="center")
fnameent.place(x=30, y=15)

lnamelbl = Label(root, text="نام خانوادگی", font=LBLFONT).place(x=330, y=70)
lnameent = Entry(root, font=ENTFONT, justify="right")
lnameent.place(x=30, y=75)

fullnamebtn = Button(
    root, text="نمایش نام", font=LBLFONT, bg="lightgreen", command=show_fullname
).place(x=180, y=150)

fullnamelbl = Label(root, text="", font=LBLFONT)
fullnamelbl.place(x=100, y=260)

root.mainloop()
# window.mainloop()
