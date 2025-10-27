a = int(input("num: "))

# print("even" if a % 2 == 0 else "odd") #trutty condition

# print("possetive" if a >= 0  else "negative")

# nested condition
if a == 0:
    print("zero")
else:
    if a % 2 == 0:
        if a >= 0:
            print("even and possetive")
        else:
            print("even and negative")
    else:
        if a >= 0:
            print("odd and possetive")
        else:
            print("odd and negative")

