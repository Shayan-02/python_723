from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    if float(heightent.get()) > 2.5:
        messagebox.showerror("واحد اشتباه", "قد خود را بر اساس متر وارد کنید")
    else:
        bmi = (float(weightent.get()) / (float(heightent.get()) * float(heightent.get())))
        if bmi < 18.5:
            messagebox.showinfo("BMI وضعیت", f"{bmi:.2f} -> کسر وزن ")
window = Tk()

window.geometry("300x450")

LBLFONT = ("vazir", 21, "bold")
ENTFONT = ("vazir", 15, "bold")

heightlbl = Label(window, text=":قد", font=LBLFONT).place(x=130, y=20)
heightent = Entry(window, font=ENTFONT)
heightent.place(x=25, y=70)
weightlbl = Label(window, text=":وزن", font=LBLFONT).place(x=120, y=120)
weightent = Entry(window, font=ENTFONT)
weightent.place(x=25, y=170)

showbmibtn = Button(window, text="BMI نمایش", font=LBLFONT, bg="pink", fg="white", command=calculate_bmi).place(x=70, y=250)


window.mainloop()