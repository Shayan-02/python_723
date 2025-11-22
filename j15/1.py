from tkinter import *


def show_fullname():
    fullname = fnameent.get() + " " + lnameent.get() + "😎"
    fullnamelbl.config(text=fullname)



root = Tk()
window = Tk()

root.title("fullname app")
root.geometry("400x400")

LBLFONT = ("vazir", 21, "bold")
ENTFONT = ("vazir", 18, "bold")

fnamelbl = Label(root, text="نام", font=LBLFONT).pack()
fnameent = Entry(root, font=ENTFONT, justify="center")
fnameent.pack()

lnamelbl = Label(root, text="نام خانوادگی", font=LBLFONT).pack()
lnameent = Entry(root, font=ENTFONT, justify="right")
lnameent.pack()

fullnamebtn = Button(root, text="نمایش نام", font=LBLFONT, bg="lightgreen", command=show_fullname).pack(pady=20)

fullnamelbl = Label(window, text="", font=LBLFONT)
fullnamelbl.pack()

root.mainloop()
window.mainloop()