def oddEven(x):
  if x % 2 == 0: return "even"
  else: return "odd"


oddOrEven = lambda x, y=10 : "odd" if x % 2 == 1 else "even"


print(oddEven(int(input())))
print(oddEven(11))

print(oddOrEven(10))
print(oddOrEven(11))