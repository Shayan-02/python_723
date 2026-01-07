with open("./1.txt", "r", encoding="utf-8") as f:
    print(f.read())

arr = ["salam", "chetori"]
with open("./2.txt", "a", encoding="utf-8") as f2:
    for i in arr:
        f2.write(i+"\n")
        f2.write("khoobi")