try:
    with open("./1.txt", "x") as f:
        f.write("salam")
except Exception as e:
    print(e)