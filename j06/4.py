tedad = 0
sumNumbers = 0
while True:
    number = int(input("enter a number: "))
    if number == -100:
        break
    else:
        if 0 <= number <= 20:
            sumNumbers += number
            tedad += 1
        else:
            print("invalid number")
            number = int(input("enter a true number: "))

print(sumNumbers/tedad)