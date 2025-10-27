num = int(input("enter a number: "))

if num % 15 == 0: print("fizzbazz")
elif num % 3 == 0: print("fizz")
elif num % 5 == 0: print("bazz")
else: print(num)