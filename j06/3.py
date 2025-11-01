run = True
tedad = 0
sumNumbers = 0
while run:
    number = int(input("enter a number: "))
    if number == -100:
        run = False
    else:
        if 0 <= number <= 20:
            sumNumbers += number
            tedad += 1
        else:
            print("invalid number")
            number = int(input("enter a true number: "))

print(sumNumbers/tedad)