from tkinter import messagebox
try:
    n = "salam" # strintg
    print(n)
    # print(int(n) * 3)
except Exception as e:
    messagebox.showerror("ValueError", e)
finally:
    print("hello")

# n = "salam" # strintg
# print(int(n) * 3)

# def test():
#     print("salam")

# a = test() * 3

# a = "salam"
# b = 2

# c = a * 2
# print(c)
# d = a + 2

print("continue")