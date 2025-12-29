from tkinter import *


def togletheme():
  global theme
  theme = "light"
  if theme == "light":
    root.config(bg="#777777")
    theme_btn.config(text="☀️")
    theme = "dark"
  elif theme == "dark":
    root.config(bg="white")
    theme_btn.config(text="🌚")
    theme = "light"

root = Tk()
root.geometry("400x500")
theme_btn = Button(root, text="", command=togletheme)
theme_btn.pack()
togletheme()

# root.config(bg="#777777")

root.mainloop()