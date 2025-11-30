from random import *

lst = []
while True:
  a = input("enter name: ")
  if a == "done":
    break
  else:
    # with open("./j16/test.txt", "a") as f:
    #   f.write(f"{a}\n")
    lst.append(a)

with open("./j16/test.txt", "a", encoding="utf-8") as f:
  for i in lst:
    f.write(f"{i}\n")

with open("./j16/test.txt") as f:
  print(choice(f.readlines()))
# print(choice(lst))