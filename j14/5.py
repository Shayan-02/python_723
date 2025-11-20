from tkinter import *

window = Tk()
window.title("first app")
window.geometry("300x450")
# window.resizable(width=1, height=0)
# window.config(bg="#e25dd7")

fname = Label(window, text="ali rezaee", font=("arial", 20, "bold"), fg="blue").place(x=50, y=100)

window.mainloop()