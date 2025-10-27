num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))



if 0 <= num1 <= 20:
    if 0 <= num2 <= 20:
        if 0 <= num3 <= 20:
            avg = (num1 + num2 + num3) / 3
            if avg >= 16:
                print("your average is ", avg, "-> A")
            elif avg >= 14:
                print("your average is ", avg, "-> B")
            elif avg >= 12:
                print("your average is ", avg, "-> C")
            elif avg >= 10:
                print("your average is ", avg, "-> D")
            else:
                print("your average is ", avg, "-> Failed")
        else:
            print("num3 is false")
    else:
        print("num2 is false")
else:
    print("num1 is false")