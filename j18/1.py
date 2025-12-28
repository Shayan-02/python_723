from tkinter import *


def showFullName():
  fname = fname_ent.get()
  lname = lname_ent.get()
  fullName = fname + " " + lname
  # print(fullName)
  fullname_lbl.config(text=fullName)


PRIMARY_FONT=("vazir", 20, "bold")
ENT_FONT=("vazir", 16, "bold")

window = Tk()
window.title("fullname app")
window.geometry("400x450")
window.resizable(0, False)
# window.config(bg="#F7567C")

# fname
fname_lbl = Label(window, text="نام", font=PRIMARY_FONT).pack()
fname_ent = Entry(window, font=ENT_FONT, justify="center")
fname_ent.pack(pady=20)

# lname
lname_lbl = Label(window, text="نام خانوادگی", font=PRIMARY_FONT).pack()
lname_ent = Entry(window, font=ENT_FONT, justify="center")
lname_ent.pack(pady=20)

# button
fullname_btn = Button(window, text="نمایش نام کامل", font=PRIMARY_FONT, bg="lightgreen", fg="darkblue", command=showFullName).pack(pady=10)

# fullname
fullname_lbl = Label(window, text="", font=PRIMARY_FONT)
fullname_lbl.pack(pady=10)

window.mainloop()