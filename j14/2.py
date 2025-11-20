import random

# a = random.randint(1, 10)

# print(a)

c = random.randint(1, 10)
def guess_number(answer : int) -> str:
    if c == a:
        return "you win"
    else:
        if c > a:
            return "enter higher"
        else:
            return "enter lower"

for i in range(3):
    a = int(input("enter a number: "))
    b = guess_number(a)
    if b == "you win":
        print(b)
        break
    else:
        print(b)
else:
    print("you loss", c)