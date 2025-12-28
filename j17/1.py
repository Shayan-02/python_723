def isEven(n) -> str:
  # print("even" if n % 2 == 0 else "odd")  # truety condition
  if n % 2 == 0:
    print("even")
  else:
    print("odd")



number = int(input("enter a number: "))
# calling function
isEven(number)